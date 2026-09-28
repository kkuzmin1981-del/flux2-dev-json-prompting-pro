# flux2-dev-json-prompting-pro

🌐 [English](readme.md) · [Русский](readme-rus.md) · [中文](readme-chn.md)

**FLUX.2 [dev] — 专业 JSON 提示词系统** — 通用智能体技能（skill），适用于任意 AI 智能体。

该技能将用户简单的需求（「桌上一杯咖啡」「雨夜霓虹街道」）转换为面向 **FLUX.2 [dev]** 文生图模型（Black Forest Labs）的技术精确、专业级 JSON 提示词 —— 使用真实的相机、镜头、布光与色彩科学术语，而非模糊的形容词。你会惊讶地发现，连贯纯文本提示词与专业 JSON 之间的差距有多大。深入体验专业级 FLUX 2。

## 技能功能

- **完整 JSON 模式** — JSON 是 FLUX 2 官方认可的专业级结构化提示词格式，模型对 JSON 的理解比连贯纯文本更精确。所有字段必填，字段顺序固定，`aspect_ratio` 置于最后，作为模型对用户选择宽高比的推荐。
- **基于参考表的术语** — 相机机身、镜头、角度、景别、焦点、光圈、ISO、胶片模拟、风格分类、构图技法、渐变句式与宽高比，全部从内置参考表选取，而非临场杜撰。
- **色彩与光线物理** — 60-30-10 色板层级（HEX 锚定）、开尔文色温、主光:补光比（key:fill），以及 SQTSI 布光框架（Source → Quality → Temperature → Shadow → Interaction，即光源 → 光质 → 色温 → 阴影 → 光线交互）。
- **先推荐后确认** — 对每个缺失参数，模型给出一个专业取值并附简短理由；用户确认（或定点修改）后才定稿。

## 文件结构

```
flux2-dev-json-prompting-pro/
├── SKILL.md              # 协议：面向 LLM 的工作流
├── handbook.md           # 技术参考表：LLM 如何填写每个字段
├── color-light.md        # 色彩与光线物理：色板、色温、光比、SQTSI
├── examples.md           # 六个完整 JSON 提示词 —— 面向 LLM 的输出格式参照
└── tools/
    └── check_prompt.py   # 机械化校验器（Python 3，仅用标准库）
```

## JSON 提示词格式

```json
{
  "scene": "",
  "subjects": [
    {
      "type": "",
      "description": "",
      "pose": "",
      "position": "",
      "action": "",
      "colors": []
    }
  ],
  "style": "",
  "color_palette": [],
  "lighting": "",
  "mood": "",
  "background": "",
  "composition": "",
  "camera": {
    "model": "",
    "angle": "",
    "lens": "",
    "f-number": "",
    "ISO": "",
    "distance": "",
    "focus": "",
    "depth_of_field": ""
  },
  "aspect_ratio": ""
}
```

## 使用方法

调用技能时，写一个普通的请求，描述你想要的画面。也可以只写几条简短的要点：

> "帮我构思一条提示词及其细节。80 年代风格，像电视剧那样：一位白人警察和一位黑人侦探是搭档，迈阿密，站在一辆车旁，夜晚，城市灯火强烈虚化，色彩丰富……"

随后模型会先在内部进行推敲，然后针对你没有指定的每一个参数给出选项 —— 每个选项都附带基于场景的简短理由 —— 并请你确认或提出修改。如果一切满意，回复 "Yes"（或指出具体修改）。之后只需等待完成 —— 最终 JSON 提示词会自动输出。

## 建议

建议使用指令遵循能力较强、不偷工减料的 LLM，例如 Qwen 3.8、GLM 等。

## 安装

让你的智能体将这个技能安装到它自己的环境中，并提供这个链接即可。

## 使用

取决于你使用的 AI 智能体。例如在 LM Studio 的 Bionic 中：`@flux2-dev-json-prompting-pro`。

## 校验器检查项

提示词的结构与所使用的字段。
