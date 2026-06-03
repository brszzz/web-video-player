# web-video-player

基于 Web 的 FLV 视频播放器，支持弹幕渲染，通过 File System Access API 播放本地文件。

## 功能

- **FLV 播放** — 使用 [flv.js](https://github.com/bilibili/flv.js) 解码 FLV 文件，通过 Media Source Extensions 播放
- **文件夹选择** — 通过 File System Access API 选择本地文件夹，自动发现 `.flv` 和弹幕文件
- **弹幕渲染** — Canvas 实时渲染弹幕，支持多轨道碰撞避让
  - 兼容 JSONL 格式（每行一个 JSON）
  - 兼容嵌套 JSON 格式（`{ "events": [...] }`）
- **Seek 重建** — 拖进度条到未缓冲区域时，自动切片文件 + 重建播放器
- **全屏模式** — 控制栏 3 秒无操作自动隐藏，移动鼠标恢复
- **暂停冻结** — 暂停时弹幕冻结在原地，播放时继续滚动
- **弹幕设置** — 密度、透明度、字号、位置、时间偏移可调

## 快速开始

```bash
# 启动本地开发服务器
python server.py

# 浏览器打开
# http://localhost:5174/player.html
```

点击页面上的文件夹图标，选择包含 `.flv` 文件的文件夹即可开始播放。

弹幕文件需放在同一文件夹下，文件名包含 `danmaku`，以 `.json` 或 `.tmp` 结尾。

## 键盘快捷键

| 键 | 功能 |
|---|---|
| `Space` | 播放 / 暂停 |
| `←` `→` | 后退 / 前进 5 秒 |
| `F` | 全屏 |
| `M` | 静音 |

## 部署到 Hexo 博客

将 `player.html` 复制到 Hexo 的 `source/video-player/index.html`，在 frontmatter 添加 `layout: false`：

```yaml
---
layout: false
---
```

在 Butterfly 主题 `_config.butterfly.yml` 中添加菜单项和注入脚本，使链接在新标签页打开。

## 目录结构

```
player.html          # 主播放器页面
server.py            # 开发用 HTTP 服务器（CORS + Range）
tests/               # Playwright 测试
```

## 依赖

- [flv.js](https://cdn.jsdelivr.net/npm/flv.js@1.6.2/dist/flv.min.js) (CDN)
- 浏览器要求：Chrome / Edge（需支持 File System Access API）
