<h1 align="center">你好，我是 autentisitet 👋</h1>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<p align="center">
  <a href="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2500&pause=900&color=58A6FF&center=true&vCenter=true&width=600&lines=ML+Engineering+%C2%B7+Computer+Vision;Inference+Systems+%C2%B7+Reproducible+Software">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2500&pause=900&color=58A6FF&center=true&vCenter=true&width=600&lines=ML+Engineering+%C2%B7+Computer+Vision;Inference+Systems+%C2%B7+Reproducible+Software" alt="机器学习工程、计算机视觉与推理系统" />
  </a>
</p>

<p align="center">
  深圳大学电子信息工程本科生 · 2027 届
</p>

我专注于构建可复现的机器学习系统，打通数据验证、模型训练、评估与推理交付。

目前主要研究图像与视频质量评价，关注可靠的数据工作流、PyTorch 模型开发，以及实用的推理服务。

## 我的方向

- **机器学习工程**——配置驱动的训练、评估、检查点管理与实验产物
- **计算机视觉**——结合空间与时序建模的图像和视频质量评价
- **推理系统**——FastAPI 服务、批量推理、容器化与 CI 验证

## 代表项目

### [deep-vqa-framework](https://github.com/autentisitet/deep-vqa-framework)

一个基于 PyTorch 的无参考图像与视频质量评价平台，覆盖数据检查、模型训练、评估和推理部署。

- 统一的 `IQAVQANet` 同时支持图像 IQA 与视频 VQA，并使用可配置的 ImageNet 主干网络和 Transformer 时序融合
- 在训练前解码输入文件进行媒体完整性检查，并隔离无法读取的样本
- 使用分组的训练/验证/测试划分与 K 折划分，降低重复参考内容造成的数据泄漏
- 结合 MOS 回归与成对排序目标，预测感知质量
- 提供覆盖 PLCC、SROCC、KROCC、RMSE、残差诊断、MOS 分箱分析、特征分布与 Grad-CAM 的评估和可解释性工作流
- 提供浏览器工作台，支持上传媒体、运行选定检查点、查看评分与历史记录，以及检查模型解释结果
- 使用 SQLite 保存内部单实例部署的评估历史，同时为受保护的公共部署提供无状态存储模式
- 可选集成 Ollama，用于生成技术质量描述和辅助主观评分，但与核心 IQA/VQA 模型保持解耦
- 使用 Docker/Podman、Nginx、健康检查、部署 profile、GitHub Actions 验证与 `uv` 管理部署环境

该项目将数据验证、泄漏控制、模型评估、产物管理和推理交付视为一套可复现的机器学习工程工作流。

## 常用技术

Python · PyTorch · OpenCV · FastAPI · SQLite · Nginx · Docker/Podman · Makefile · GitHub Actions · Bash

## 贡献轨迹

<div align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake-mobile-dark.svg">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake.svg">
    <img width="100%" alt="GitHub 贡献网格贪吃蛇动画" src="https://raw.githubusercontent.com/autentisitet/autentisitet/output/github-contribution-grid-snake.svg">
  </picture>
</div>

## 期望方向

寻找机器学习工程、计算机视觉、推理系统，或 AI 产品后端工程方向的初级岗位或实习机会。

我重视可复现性、清晰的接口设计，以及让机器学习工作流更易于运行和维护。

## 联系我

可以通过 [icey08852@gmail.com](mailto:icey08852@gmail.com) 联系我。
