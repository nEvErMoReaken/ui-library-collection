# UI Library Collection

个人收集的 UI 库 / 组件库 / 设计系统链接，按分类整理。

共收录 **7** 个库，最后更新于 2026-09-17。

## 目录

- [Shadcn 核心生态](#shadcn-核心生态) (1)
- [Shadcn 兼容扩展](#shadcn-兼容扩展) (4)
- [独立非 Shadcn 库](#独立非-shadcn-库) (2)

## Shadcn 核心生态

> 深度绑定 shadcn/ui：必须先用 `shadcn` CLI 初始化项目，组件通过 `npx shadcn add` 安装，代码风格/约定与 shadcn 一致。

| 名称 | 框架 | 链接 | 说明 | 收费 | 标签 | 来源 | 添加日期 |
|---|---|---|---|---|---|---|---|
| Spectrum UI | React | [https://ui.spectrumhq.in/](https://ui.spectrumhq.in/) | 基于 shadcn/ui 扩展的独立组件库，250+ 个产品级动画组件/区块（看板、多步表单、密码强度条、通知铃等）。技术栈: React+Next.js+TypeScript+Tailwind+Radix UI+Framer Motion，用 shadcn CLI 作安装通道（npx shadcn add @spectrumui/xxx），官方明确表示'扩展而非替代shadcn，两者设计成一起用'。附带 MCP server 供 AI agent 调用 | Free / Open Source | radix, motion, animation, mcp, product-ui |  | 2026-09-17 |

## Shadcn 兼容扩展

> 独立组件库，但额外提供 shadcn CLI 作为可选安装通道；不依赖 shadcn 项目也能用（可直接 copy-paste）。

| 名称 | 框架 | 链接 | 说明 | 收费 | 标签 | 来源 | 添加日期 |
|---|---|---|---|---|---|---|---|
| Animate UI | React | [https://github.com/imskyleen/animate-ui](https://github.com/imskyleen/animate-ui) | 完全动画化的开源组件分发库，基于 React + TypeScript + Tailwind CSS + Motion，兼容 Shadcn CLI，可浏览并一键安装/修改动画组件 | Free / Open Source | animation, tailwind, motion, copy-paste |  | 2026-09-17 |
| Cult UI | React | [https://www.cult-ui.com/](https://www.cult-ui.com/) | 面向设计工程师(Design Engineers)打造的组件库，Tailwind CSS 样式，完全兼容 Shadcn，copy-paste 即用，MIT 许可 | Free / Open Source | tailwind, copy-paste, design-engineering |  | 2026-09-17 |
| React Bits | React | [https://reactbits.dev/](https://reactbits.dev/) | 开源的创意型 React 动画组件库，165+ 个组件（文字动效、背景特效、UI元素），非常规组件库——不提供按钮/输入框等基础元素，专注视觉惊艳的动效展示。每个组件提供4种变体(JS-CSS/JS-TW/TS-CSS/TS-TW)，支持 shadcn CLI 和 jsrepo 安装，模块化按需引入不产生依赖 | Free / Open Source | animation, creative, copy-paste, text-effects, backgrounds |  | 2026-09-17 |
| Vue Bits | Vue | [https://vue-bits.dev/](https://vue-bits.dev/) | React Bits 的官方 Vue 移植版，130+ 个创意动画组件（背景特效、文字动效、UI交互模式），TypeScript + Tailwind 编写，通过 jsrepo/shadcn CLI 一键安装到项目中，AI 友好（适配 Cursor/Copilot/v0） | Free / Open Source | animation, creative, copy-paste, text-effects, backgrounds |  | 2026-09-17 |

## 独立非 Shadcn 库

> 完全自成体系，与 shadcn 无关，有自己的安装方式和设计语言。

| 名称 | 框架 | 链接 | 说明 | 收费 | 标签 | 来源 | 添加日期 |
|---|---|---|---|---|---|---|---|
| Prompt Kit | React | [https://github.com/ibelick/prompt-kit](https://github.com/ibelick/prompt-kit) | 专为 AI 应用界面打造的核心构建组件库，高质量、可访问(a11y)、可自定义，适合聊天/对话类 AI 产品 UI | Free / Open Source | ai-ui, components, accessible |  | 2026-09-17 |
| Watermelon UI | React | [https://ui.watermelon.sh/](https://ui.watermelon.sh/) | Watermelon UI（@watermelonui）是一个专为初创团队和开发者打造的 React UI 组件库：750+ 高质量组件，整体风格偏向**多邻国(Duolingo)式的游戏化(gamification)风格**——圆润饱满的形状、鲜艳明快的配色、卡通化图标和拟物化 3D 感、带弹跳/反馈感的过渡动效，适合做产品打卡、成就徽章、进度条等游戏化交互界面。组件涵盖动画交互组件、Bento 网格、轮播/卡片滑动、日历小组件、Blocks（Hero区块/认证模板/Footer/博客布局）、完整仪表盘和模板，可直接 copy-paste 到项目里，主打“设计到开发零损耗”。100% 开源，官方在站点标注了每个组件的设计灵感来源以示尊重原创。附带 AI 辅助 prompt（vibe coding）、llms.txt/OpenAPI/MCP 接口，方便 AI agent 直接检索和使用组件库。 | Free / Open Source | components, templates, dashboard, mcp, animation, bento, copy-paste, gamified, duolingo-style, playful | [link](https://twitter.com/xin_pai88825/status/2100483741768675527) | 2026-09-17 |

---

数据源见 [`data/libraries.json`](data/libraries.json)，由脚本 [`scripts/generate_readme.py`](scripts/generate_readme.py) 自动生成本文件，请勿手动编辑表格内容。
