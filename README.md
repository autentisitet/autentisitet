<h1 align="center">Hi, I'm autentisitet 👋</h1>

<p align="center">
  <strong>English</strong> · <a href="README_zh.md">简体中文</a>
</p>

<p align="center">
  <a href="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2500&pause=900&color=58A6FF&center=true&vCenter=true&width=600&lines=ML+Engineering+%C2%B7+Computer+Vision;Reproducible+Software+%C2%B7+Repo+Quality">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2500&pause=900&color=58A6FF&center=true&vCenter=true&width=600&lines=ML+Engineering+%C2%B7+Computer+Vision;Reproducible+Software+%C2%B7+Repo+Quality" alt="ML Engineering, Computer Vision, Reproducible Software" />
  </a>
</p>

<p align="center">
  Electronic Information Engineering undergraduate at Shenzhen University · Class of 2027
</p>

I build reproducible machine-learning systems and the engineering tooling around them. My current
focus is image and video quality assessment (IQA/VQA) end to end: data validation,
model training, evaluation, interpretability, and a FastAPI + Nginx deployment.

## What I build

- **ML engineering** — configuration-driven training, evaluation, checkpoints, and experiment artifacts
- **Computer vision** — image and video quality assessment with spatial and temporal modeling
- **Serving & deployment** — FastAPI services, batch inference, Docker/Podman, Nginx, and CI validation

---

## Featured projects

### [deep-vqa-framework](https://github.com/autentisitet/deep-vqa-framework)

A PyTorch platform for image and video quality assessment, covering data checks,
model training, evaluation, and inference deployment.

- A unified `IQAVQANet` for image IQA and video VQA, using configurable ImageNet backbones and Transformer-based temporal fusion
- Media integrity checks that decode inputs before training and isolate unreadable samples
- Group-aware train/validation/test and K-fold splitting to reduce leakage from repeated reference content
- A hybrid MOS regression and pairwise-ranking objective for quality prediction
- Evaluation and interpretability workflows covering PLCC, SROCC, KROCC, RMSE, residual diagnostics, MOS-bin analysis, feature distributions, and Grad-CAM
- A browser workbench for uploading media, running selected checkpoints, viewing scores and history, and inspecting model interpretations
- SQLite-backed evaluation history for internal single-instance deployments, with a stateless storage mode for protected public deployments
- Docker/Podman deployment with Nginx, health checks, deployment profiles, GitHub Actions validation, and `uv`-managed environments

### [repo-maintenance-skills](https://github.com/autentisitet/repo-maintenance-skills)

A set of Codex skills that turn common engineering conventions into reusable workflows, covering
documentation, GitHub Actions hardening, repository hygiene, project layout, frontend/backend
quality, and Docker/Podman deployment.

---

## Tech I use most

Python · PyTorch · OpenCV · FastAPI · SQLite · Nginx · Docker/Podman · Makefile · GitHub Actions · Bash

---

## Contribution trail

<div align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake-mobile-dark.svg">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake.svg">
    <img width="100%" alt="GitHub contribution grid snake animation" src="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake.svg">
  </picture>
</div>

---

## What I'm looking for

Entry-level roles or internships in ML engineering, computer vision, or backend engineering.

I care about reproducibility, clear interfaces, and making ML workflows easier to run and maintain.

---

## Let's connect

Reach me at [icey08852@gmail.com](mailto:icey08852@gmail.com).
