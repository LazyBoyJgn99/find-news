# Find News

多引擎搜索 API 工具，支持通用网页搜索和新闻搜索。**开箱即用，无需配置**。

## 功能特性

- 支持多个搜索引擎：Google、Baidu、Bing、Yahoo、DuckDuckGo
- 支持社交媒体和平台搜索：微信公众号、YouTube、GitHub、Reddit、Bilibili
- 新闻搜索功能
- 可选的完整内容抓取
- 智能缓存机制（30分钟内相同查询免费）

## 快速开始

直接使用，无需任何配置：

```bash
python3 scripts/search.py search "测试" -n 3
```

## 使用示例

### 通用搜索
```bash
python3 scripts/search.py search "人工智能" -s baidu -n 5
```

### 新闻搜索
```bash
python3 scripts/search.py news "科技新闻" -s google -n 10
```

### 微信公众号搜索
```bash
python3 scripts/search.py search "Python教程" -s wechat -n 5
```

### GitHub 代码搜索
```bash
python3 scripts/search.py search "react hooks" -s github -n 10
```

## 详细文档

查看 [SKILL.md](./SKILL.md) 获取完整的使用说明和 API 文档。

## 注意事项

- 默认使用 `crawl_results=0` 以获得快速响应
- 设置 `crawl_results > 0` 会显著增加延迟（10-30秒/页）
- 每个搜索结果成本 10 积分，缓存命中免费
- 相同查询 30 分钟内会使用缓存，免费且更快

## 高级配置（可选）

如果需要使用自己的 API 服务，可以设置环境变量：

```bash
export SEARCH_API_KEY="your_api_key_here"
export SEARCH_API_BASE_URL="http://your-server:3000"
```

脚���会优先使用环境变量中的配置。
