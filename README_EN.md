# Research Workbench: NIR · Chemometrics · Nature-Style Papers

![skills](https://img.shields.io/badge/skills-19-0ea5e9)
![focus](https://img.shields.io/badge/focus-NIR%20%7C%20Chemometrics%20%7C%20Scientific%20Writing-111827)
![license](https://img.shields.io/badge/license-Apache--2.0-2ea44f)

This is a research-focused adaptation of [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills). The original skills are preserved, while the day-to-day entry point is reorganized around a reproducible workflow for **near-infrared spectroscopy, chemometrics, feature selection, robust modeling, scientific figures, manuscript writing, reference verification, and peer-review response**.

Chinese research homepage: [README.md](README.md)

## 1. Primary Research Workflow

| Stage | Goal | Preferred Skill |
|---|---|---|
| Literature search | Find real papers on NIR, chemometrics, feature selection, robustness, and model transfer | `nature-academic-search` |
| Paper reading | Extract samples, instrument, algorithms, figures, innovations, and limitations | `nature-reader` |
| Citation control | DOI formatting and reference verification | `nature-citation` + `nature-ref-verifier` |
| Data and experiments | Reproducible data handling and experiment logging | `nature-data` + `nature-experiment-log` |
| Statistics | Cross-validation, uncertainty, stability, and fair model comparison | `nature-statistics` |
| Figures | Spectra, feature-frequency plots, performance plots, multipanel figures | `nature-figure` |
| Writing | Methods, Results, Discussion, Introduction, Abstract | `nature-writing` |
| Polishing | Nature-family academic English | `nature-polishing` |
| Pre-submission audit | Reviewer-style critique | `nature-reviewer` |
| Revision | Point-by-point reviewer responses | `nature-response` |

Main NIR workflow: [research-workbench/nir-chemometrics/WORKFLOW.md](research-workbench/nir-chemometrics/WORKFLOW.md)

Reusable prompts: [research-workbench/nir-chemometrics/PROMPTS.md](research-workbench/nir-chemometrics/PROMPTS.md)

Figure standards: [research-workbench/nir-chemometrics/FIGURE_STANDARD.md](research-workbench/nir-chemometrics/FIGURE_STANDARD.md)

## 2. Modeling Principles

1. Feature selection and hyperparameter tuning must stay inside the training/calibration data.
2. Prefer nested cross-validation for unbiased performance estimation.
3. Do not report only a single best stochastic run; report distributions and stability.
4. Keep a full-spectrum baseline.
5. Algorithmic modifications must solve a concrete scientific or statistical problem rather than simply stack optimizers.
6. Spectral assignments require real supporting references.

## 3. Skill Index

The complete set of triggerable skills is retained below. `nature-shared` remains a support-only package and is intentionally excluded from the triggerable count.

| Skill | Purpose |
|---|---|
| [`nature-academic-search`](skills/nature-academic-search/README_EN.md) | Multi-source academic search and evidence chains |
| [`nature-citation`](skills/nature-citation/README_EN.md) | Citation and reference management |
| [`nature-data`](skills/nature-data/README_EN.md) | Data governance and availability |
| [`nature-downloader`](skills/nature-downloader/README_EN.md) | Literature download assistance |
| [`nature-experiment-log`](skills/nature-experiment-log/README_EN.md) | Experiment logging and traceability |
| [`nature-figure`](skills/nature-figure/README_EN.md) | Publication-grade scientific figures |
| [`nature-image2ppt`](skills/nature-image2ppt/README_EN.md) | Image-based slide reconstruction |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README_EN.md) | Automated literature workflows |
| [`nature-paper-card`](skills/nature-paper-card/README_EN.md) | Structured deep-reading paper cards |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README_EN.md) | Paper-to-patent drafting support |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README_EN.md) | Paper-to-presentation workflow |
| [`nature-polishing`](skills/nature-polishing/README_EN.md) | Academic English polishing |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README_EN.md) | Proposal and research-plan writing |
| [`nature-reader`](skills/nature-reader/README_EN.md) | Paper reading and structured extraction |
| [`nature-ref-verifier`](skills/nature-ref-verifier/README_EN.md) | Reference verification |
| [`nature-response`](skills/nature-response/README_EN.md) | Reviewer-response packages |
| [`nature-reviewer`](skills/nature-reviewer/README_EN.md) | Pre-submission reviewer simulation |
| [`nature-statistics`](skills/nature-statistics/README_EN.md) | Statistical analysis and reporting |
| [`nature-writing`](skills/nature-writing/README_EN.md) | Scientific manuscript writing |

## 4. Personal Research Workbench

```text
research-workbench/
├─ README.md
└─ nir-chemometrics/
   ├─ WORKFLOW.md
   ├─ PROMPTS.md
   ├─ FIGURE_STANDARD.md
   └─ research-profile.yaml
```

Suggested project layout:

```text
project-name/
├─ data_raw/
├─ data_processed/
├─ splits/
├─ models/
├─ results/
├─ figures/
├─ tables/
├─ scripts/
├─ literature/
└─ manuscript/
```

## 5. Upstream and License

This repository is adapted from the open-source project [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills). Original code, resources, and attribution remain in repository history and source files. Redistribution and use should follow [LICENSE](LICENSE).
