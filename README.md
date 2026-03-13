# Find News

多引擎搜索 API 工具，支持通用网页搜索和新闻搜索。

## 功能特性

- 支持多个搜索引擎：Google、Baidu、Bing、Yahoo、DuckDuckGo
- 支持社交媒体和平台搜索：微信公众号、YouTube、GitHub、Reddit、Bilibili
- 新闻搜索功能
- 可选的完整内容抓取
- 智能缓存机制（30分钟内相同查询免费）

## 快速开始

### 前置条件

1. 启动 Search API 服务（在另一个终端）：
   ```bash
   cd /path/to/search-api-server
   npm start
   # 默认监听在 http://localhost:3000
   ```

2. 设置环境变量：
   ```bash
   export SEARCH_API_KEY="your_api_key_here"
   # 可选：自定义 API 地址
   export SEARCH_API_BASE_URL="http://localhost:3000"
   ```

3. 测试连接：
   ```bash
   python3 scripts/search.py search "测试" -n 1
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
- 每个搜索结果成本 ¥0.10，缓存命中免费
- 请妥善保管 API Key，不要提交到 git 仓库
