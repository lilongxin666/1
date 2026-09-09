from __future__ import annotations

import csv
import json
import re
import shutil
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path("work/extracted")
OUT = Path("work/organized")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "by_sample").mkdir(exist_ok=True)
(OUT / "raw_headers").mkdir(exist_ok=True)
(OUT / "supplementary").mkdir(exist_ok=True)


def safe_name(s: str) -> str:
    s = s.strip().replace("\ufeff", "")
    s = re.sub(r"[^0-9A-Za-z_\-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "meta"


def unique_names(names):
    out, seen = [], {}
    for name in names:
        base = safe_name(name)
        n = seen.get(base, 0)
        seen[base] = n + 1
        out.append(base if n == 0 else f"{base}_{n+1}")
    return out


spectra_dirs = [p for p in ROOT.rglob("*") if p.is_dir() and p.name.lower() == "spectra"]
if not spectra_dirs:
    raise RuntimeError("No Spectra directory found after extraction.")
spectra_dir = spectra_dirs[0]
csv_files = sorted(spectra_dir.glob("*.csv"))
if not csv_files:
    raise RuntimeError(f"No CSV files found in {spectra_dir}")

print(f"Using spectra directory: {spectra_dir}")
print(f"Found {len(csv_files)} spectral CSV files")
for p in csv_files:
    print("  ", p.name)

all_frames = []
metadata_frames = []
summaries = []
reference_wavelengths = None
reference_wavelength_labels = None
mismatch_files = []

for fpath in csv_files:
    # The authors' validation code reads numerical spectra with skiprows=7.
    with fpath.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        reader = csv.reader(fh)
        header_rows = []
        for _ in range(7):
            try:
                header_rows.append(next(reader))
            except StopIteration:
                break

    with (OUT / "raw_headers" / f"{safe_name(fpath.stem)}_header7.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as fh:
        csv.writer(fh).writerows(header_rows)

    dat = pd.read_csv(fpath, header=None, skiprows=7, engine="python")
    dat = dat.apply(pd.to_numeric, errors="coerce").dropna(how="all")
    dat = dat.dropna(axis=1, how="all")
    if dat.shape[1] < 2:
        raise RuntimeError(f"Unexpected numeric shape in {fpath}: {dat.shape}")

    wavelengths = dat.iloc[:, 0].to_numpy(dtype=float)
    spectra = dat.iloc[:, 1:].to_numpy(dtype=np.float32).T
    valid_w = np.isfinite(wavelengths)
    wavelengths = wavelengths[valid_w]
    spectra = spectra[:, valid_w]

    wl_labels = []
    for x in wavelengths:
        if abs(x - round(x)) < 1e-6:
            wl_labels.append(str(int(round(x))))
        else:
            wl_labels.append(f"{x:.6f}".rstrip("0").rstrip("."))

    if reference_wavelengths is None:
        reference_wavelengths = wavelengths.copy()
        reference_wavelength_labels = wl_labels
    else:
        same = len(wavelengths) == len(reference_wavelengths) and np.allclose(
            wavelengths, reference_wavelengths, rtol=0, atol=1e-8, equal_nan=False
        )
        if not same:
            mismatch_files.append(fpath.name)
            raise RuntimeError(
                f"Wavelength grid mismatch in {fpath.name}. No silent interpolation is performed."
            )

    n_spectra = spectra.shape[0]
    raw_keys = []
    for ridx, row in enumerate(header_rows):
        first = row[0].strip() if row else ""
        raw_keys.append(first if first else f"header_{ridx+1}")
    meta_keys = unique_names(raw_keys)

    material_group = "coal" if "coal" in fpath.stem.lower() else "rock"
    meta = {
        "sample_name": [fpath.stem] * n_spectra,
        "material_group": [material_group] * n_spectra,
        "spectrum_index_within_sample": np.arange(1, n_spectra + 1, dtype=int),
        "source_file": [fpath.name] * n_spectra,
    }
    for ridx, key in enumerate(meta_keys):
        row = header_rows[ridx] if ridx < len(header_rows) else []
        vals = row[1:]
        if len(vals) < n_spectra:
            vals = vals + [""] * (n_spectra - len(vals))
        meta[f"meta_{key}"] = vals[:n_spectra]

    meta_df = pd.DataFrame(meta)
    spec_df = pd.DataFrame(spectra, columns=reference_wavelength_labels)
    combined = pd.concat([meta_df.reset_index(drop=True), spec_df], axis=1)

    out_name = safe_name(fpath.stem)
    combined.to_csv(
        OUT / "by_sample" / f"{out_name}_spectra.csv.gz",
        index=False,
        compression="gzip",
    )
    metadata_frames.append(meta_df)
    all_frames.append(combined)

    summaries.append(
        {
            "sample_name": fpath.stem,
            "material_group": material_group,
            "n_spectra": int(n_spectra),
            "n_wavelengths": int(len(reference_wavelengths)),
            "wavelength_min_nm": float(np.nanmin(reference_wavelengths)),
            "wavelength_max_nm": float(np.nanmax(reference_wavelengths)),
            "source_file": fpath.name,
        }
    )

all_df = pd.concat(all_frames, ignore_index=True)
metadata_df = pd.concat(metadata_frames, ignore_index=True)
summary_df = pd.DataFrame(summaries)

all_df.insert(0, "global_spectrum_id", np.arange(1, len(all_df) + 1, dtype=int))
metadata_df.insert(0, "global_spectrum_id", np.arange(1, len(metadata_df) + 1, dtype=int))

all_df.to_csv(OUT / "Coal_NIR_All.csv.gz", index=False, compression="gzip")
metadata_df.to_csv(OUT / "Coal_NIR_Metadata.csv", index=False, encoding="utf-8-sig")
summary_df.to_csv(OUT / "Coal_NIR_SampleSummary.csv", index=False, encoding="utf-8-sig")
pd.DataFrame({"wavelength_nm": reference_wavelengths}).to_csv(
    OUT / "Coal_NIR_Wavelengths.csv", index=False, encoding="utf-8-sig"
)

coal_df = all_df[all_df["material_group"] == "coal"]
rock_df = all_df[all_df["material_group"] == "rock"]
coal_df.to_csv(OUT / "Coal_NIR_CoalOnly.csv.gz", index=False, compression="gzip")
rock_df.to_csv(OUT / "Coal_NIR_RockOnly.csv.gz", index=False, compression="gzip")

for wanted in ("Documentation", "Analysis"):
    matches = [p for p in ROOT.rglob("*") if p.is_dir() and p.name.lower() == wanted.lower()]
    if matches:
        dst = OUT / "supplementary" / wanted
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(matches[0], dst)

manifest = {
    "source_title": "A near infrared spectroscopy dataset of coal and coal-measure rock under diverse conditions",
    "source_doi": "10.5281/zenodo.11137126",
    "source_record": "https://zenodo.org/records/11137126",
    "source_archive_md5": "26ff36e5d59ddae1862eb887f728a5ae",
    "spectral_csv_count": len(csv_files),
    "total_spectra": int(len(all_df)),
    "coal_spectra": int(len(coal_df)),
    "rock_spectra": int(len(rock_df)),
    "wavelength_count": int(len(reference_wavelengths)),
    "wavelength_min_nm": float(np.nanmin(reference_wavelengths)),
    "wavelength_max_nm": float(np.nanmax(reference_wavelengths)),
    "wavelength_grid_mismatch_files": mismatch_files,
    "notes": [
        "Each row in Coal_NIR_All.csv.gz is one spectrum.",
        "Columns before the wavelength columns contain sample identity and preserved header metadata.",
        "The seven Avantes header rows are also saved unchanged under raw_headers/.",
        "No wavelength interpolation, smoothing, normalization, SNV, MSC, or derivative preprocessing was applied.",
        "material_group is inferred from filename: names containing 'coal' are coal; remaining sample files are labeled rock.",
    ],
}
(OUT / "dataset_manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
)

readme = f"""Coal / coal-measure rock NIR dataset — organized copy
==================================================

Official source
---------------
DOI: 10.5281/zenodo.11137126
Official archive MD5: 26ff36e5d59ddae1862eb887f728a5ae

Files produced
--------------
Coal_NIR_All.csv.gz
    One row = one spectrum; metadata columns first, wavelength columns after them.
Coal_NIR_Metadata.csv
    Metadata only; same global_spectrum_id as Coal_NIR_All.csv.gz.
Coal_NIR_Wavelengths.csv
    Wavelength axis in nm.
Coal_NIR_SampleSummary.csv
    Number of spectra per named coal / coal-measure rock sample.
Coal_NIR_CoalOnly.csv.gz
    Coal-only spectra.
Coal_NIR_RockOnly.csv.gz
    Coal-measure-rock spectra.
by_sample/
    One gzip-compressed analysis-ready CSV for each named material.
raw_headers/
    The original seven metadata/header rows from every spectral CSV.
supplementary/
    Original Documentation and Analysis folders, when present.
dataset_manifest.json
    Machine-readable provenance and dataset dimensions.

Processing policy
-----------------
* No spectral preprocessing was applied.
* No interpolation was performed during organization.
* Numeric spectral values are preserved; float32 is used in the organized spectrum table.
* The first seven source rows are preserved because the authors' validation code reads numerical spectra with skiprows=7.

Verified dimensions from this run
---------------------------------
Spectral CSV files: {len(csv_files)}
Total spectra: {len(all_df)}
Coal spectra: {len(coal_df)}
Rock spectra: {len(rock_df)}
Wavelength variables: {len(reference_wavelengths)}
Wavelength range: {float(np.nanmin(reference_wavelengths)):.3f}–{float(np.nanmax(reference_wavelengths)):.3f} nm
"""
(OUT / "README_dataset.txt").write_text(readme, encoding="utf-8")

print("\n=== ORGANIZATION SUMMARY ===")
print(summary_df.to_string(index=False))
print("\nTotal spectra:", len(all_df))
print("Coal spectra:", len(coal_df))
print("Rock spectra:", len(rock_df))
print(
    "Wavelengths:",
    len(reference_wavelengths),
    f"({reference_wavelengths.min()} - {reference_wavelengths.max()} nm)",
)
print("\nMetadata columns:")
print(list(metadata_df.columns))
