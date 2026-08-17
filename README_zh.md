<h1 align="center">你好，我是 autentisitet 👋</h1>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<p align="center">
  <a href="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2500&pause=900&color=58A6FF&center=true&vCenter=true&width=600&lines=ML+Systems+%C2%B7+Infrastructure+%C2%B7+Automation;Building+systems+that+actually+get+used.">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2500&pause=900&color=58A6FF&center=true&vCenter=true&width=600&lines=ML+Systems+%C2%B7+Infrastructure+%C2%B7+Automation;Building+systems+that+actually+get+used." alt="机器学习系统、基础设施与自动化" />
  </a>
</p>

<p align="center">
  电子信息工程本科生 · 机器学习工程 · 图像与视频质量评价
</p>

---

## 目录

- [我的方向](#我的方向)
- [代表项目](#代表项目)
- [常用技术](#常用技术)
- [贡献轨迹](#贡献轨迹)
- [联系我](#联系我)

我是深圳大学电子信息工程专业本科生（2023–2027）。我主要开发训练流水线、推理服务、评估框架，以及连接这些环节的自动化工具。

目前，我将这些工作应用于图像与视频质量评价。更广泛地说，我希望构建可复现、易维护且真正实用的机器学习软件。

## 我的方向

- **机器学习系统**——训练流水线、配置驱动的实验、评估工作流与推理服务
- **基础设施与自动化**——容器、CI 流水线、可复现环境与开发者工具
- **计算机视觉应用**——以图像和视频质量评价为实践场景，开展端到端机器学习工程

## 代表项目

### [deep-vqa-framework](https://github.com/autentisitet/deep-vqa-framework)

一个面向图像质量评价（IQA）与视频质量评价（VQA）的配置驱动深度学习框架。

- 为四维图像和五维视频输入提供统一的 PyTorch 模型接口
- 使用 Swin-T 提取图像与视频质量特征
- 对视频输入进行时序特征聚合
- 通过 YAML 配置实验，并支持分组 K 折交叉验证（默认五折）
- 为 TID2013 和 KoNViD-1k 提供数据加载、验证、训练与评估工作流
- 提供 FastAPI 和 CLI 推理，并在启动时加载检查点
- 使用 Docker/Podman、GitHub Actions CI 和 `uv` 管理依赖与运行环境

该项目将数据验证、模型训练、评估、检查点管理和推理服务整合到一套可复现的工作流中。

## 常用技术

Python · PyTorch · FastAPI · Docker · GitHub Actions · Bash · Makefile

## 贡献轨迹

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake.svg">
    <img width="100%" alt="GitHub 贡献网格贪吃蛇动画" src="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake.svg">
  </picture>
</div>

## 联系我

我正在寻找机器学习系统、基础设施、平台工程或开发者工具方向的初级工程师岗位或实习机会。

我重视代码质量、可复现性，以及让复杂工作流更易于运行和维护。

可以通过 [icey08852@gmail.com](mailto:icey08852@gmail.com) 联系我。
