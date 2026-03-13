# Find News

多引擎搜索 API 工具，支持通用网页搜索和新闻搜索。**开箱即用，无需配置**。

## 安装

### 作为 AI Agent Skill 安装

```bash
# 方式 1: 通过 GitHub 用户名/仓库名
npx skills add LazyBoyJgn99/find-news

# 方式 2: 通过完整 URL
npx skills add https://github.com/LazyBoyJgn99/find-news

# 全局安装
npx skills add LazyBoyJgn99/find-news -g

# 安装到所有 agents
npx skills add LazyBoyJgn99/find-news --all
```

安装后，AI Agent（如 Claude Code、Cursor）可以直接调用此 skill 进行多引擎搜索。

## 功能特性

- 支持多个搜索引擎：Google、Baidu、Bing、Yahoo、DuckDuckGo
- 支持社交媒体和平台搜索：微信公众号、YouTube、GitHub、Reddit、Bilibili
- 新闻搜索功能
- 可选的完整内容抓取
- 智能缓存机制（30分钟内相同查询免费）
- 跨平台支持（Windows/Mac/Linux）

## 使用示例

安装后，AI Agent 会自动调用 API 进行搜索。API 详情请查看 [SKILL.md](./SKILL.md)。

### API 端点

- 搜索接口：`POST http://36.151.144.35:3001/api/v1/search`
- 新闻接口：`POST http://36.151.144.35:3001/api/v1/news`

### 支持的搜索服务

- 通用搜索：`baidu`、`google`、`bing`、`duckduckgo`、`yahoo`
- 社交媒体：`wechat`（微信公众号）、`youtube`、`bilibili`
- 开发平台：`github`、`reddit`

## 详细文档

查看 [SKILL.md](./SKILL.md) 获取完整的使用说明和 API 文档。

## 注意事项

- 默认使用 `crawl_results: 0` 以获得快速响应
- 设置 `crawl_results > 0` 会显著增加延迟（10-30秒/页）
- 每个搜索结果成本 10 积分，缓存命中免费
- 相同查询 30 分钟内会使用缓存，免费且更快

## 定价

- 每个搜索结果：10 积分
- 缓存命中：免费
- 相同查询 30 分钟内第二次调用免费

## 贡献

欢迎提交 Issue 和 Pull Request！

## License

MIT
