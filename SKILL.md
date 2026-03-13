---
name: find-news
description: |
  多引擎搜索 API 工具，支持通用网页搜索和新闻搜索。
  使用场景：
  - 用户要求搜索网页、新闻、社交媒体内容
  - 需要从 Google/Baidu/Bing/Yahoo/DuckDuckGo 搜索
  - 需要搜索微信公众号、YouTube、GitHub、Reddit、Bilibili
  - 需要获取搜索结果的完整内容（crawl_results > 0）
  - 需要最新新闻和热点追踪
---

# Find News 技能

## 概述

这个技能提供多引擎搜索能力，通过调用官方 API 实现快速搜索。**开箱即用，无需配置**。

## 快速开始

直接使用即可，无需任何配置：

```bash
python3 scripts/search.py search "测试" -n 3
```

如果看到搜索结果，说明一切正常！

## 搜索脚本使用

### 位置

`scripts/search.py`

### 通用搜索 (search)

```bash
python3 scripts/search.py search "关键词" -s baidu -n 5 -c 0
```

参数说明：

- `query` (必需): 搜索关键词
- `-s, --service`: 搜索服务（对应 API 的 `search_service` 参数）
  - `baidu` (默认): 百度搜索
  - `google`: Google 搜索
  - `bing`: Bing 搜索
  - `duckduckgo`: DuckDuckGo
  - `yahoo`: Yahoo 搜索
  - `wechat`: 微信公众号
  - `youtube`: YouTube
  - `github`: GitHub
  - `reddit`: Reddit
  - `bilibili`: 哔哩哔哩
- `-n, --max-results`: 返回结果数量（对应 API 的 `max_results` 参数，1-20，默认 **3**）
- `-c, --crawl-results`: 爬取完整内容的结果数（对应 API 的 `crawl_results` 参数，0-10，默认 **0**，**仅在需要时设置**）
  - `0`: 只返回搜索摘要（快速）
  - `1-10`: 爬取完整页面内容（慢，成本高）

### 新闻搜索 (news)

```bash
python3 scripts/search.py news "关键词" -s google -n 10 -c 0
```

参数说明：

- `-s, --service`: 新闻服务（对应 API 的 `search_service` 参数）
  - `google` (默认): Google News
  - `bing`: Bing News
  - `duckduckgo`: DuckDuckGo News
  - `yahoo`: Yahoo News

## 使用示例

### 1. 快速搜索（推荐）

```bash
# 只获取搜索摘要（快速，0.5-2秒）
python3 scripts/search.py search "人工智能" -s wechat -n 5
```

### 2. 深度内容抓取（慎用）

```bash
# 获取完整页面内容（慢，10-30秒/页，成本高）
python3 scripts/search.py news "科技新闻" -s bing -n 5 -c 5
```

### 3. GitHub 代码搜索

```bash
python3 scripts/search.py search "react hooks" -s github -n 10
```

### 4. YouTube 视频搜索

```bash
python3 scripts/search.py search "tutorial" -s youtube -n 5
```

## 使用场景

### 场景 1: 快速获取搜索摘要（默认，推荐）

**用户**: "帮我搜索一下最新的 AI 新闻"
**Agent**:

```bash
python3 scripts/search.py news "AI" -s google -n 5
```

→ 返回 5 条新闻标题和摘要（**快速，0.5秒，每条 10 积分**）

### 场景 2: 深度内容抓取（仅在必要时使用）

**用户**: "我需要这篇文章的完整内容"
**Agent**:

```bash
python3 scripts/search.py search "文章标题" -n 1 -c 1
```

→ 返回完整页面内容（**慢，10-30秒，成本 10 积分**）

### 场景 3: 多平台搜索

**用户**: "在微信公众号和 B 站搜索'Python 教程'"
**Agent**:

```bash
python3 scripts/search.py search "Python教程" -s wechat -n 5
python3 scripts/search.py search "Python教程" -s bilibili -n 5
```

## API 详情

### 搜索接口

- **URL**: `POST http://36.151.144.35:3001/api/v1/search`
- **认证**: `Bearer sk_test_a6f84bf78896f10b2d28aebd7857744c`

**请求参数**:

- `query` (string, 必需): 搜索关键词
- `search_service` (string, 必需): 搜索服务名称
  - `baidu`: 百度搜索
  - `google`: Google 搜索
  - `bing`: Bing 搜索
  - `duckduckgo`: DuckDuckGo
  - `yahoo`: Yahoo 搜索
  - `wechat`: 微信公众号
  - `youtube`: YouTube
  - `github`: GitHub
  - `reddit`: Reddit
  - `bilibili`: 哔哩哔哩
- `max_results` (number, 可选): 返回结果数量 (1-20, 默认 3)
- `crawl_results` (number, 可选): 爬取完整内容的结果数 (0-10, 默认 0)

**示例**:

```bash
curl -s "http://36.151.144.35:3001/api/v1/search" \
  -H "Authorization: Bearer sk_test_a6f84bf78896f10b2d28aebd7857744c" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "龙虾",
    "search_service": "wechat",
    "max_results": 3,
    "crawl_results": 0
  }'
```

### 新闻接口

- **URL**: `POST http://36.151.144.35:3001/api/v1/news`
- **认证**: `Bearer sk_test_a6f84bf78896f10b2d28aebd7857744c`

### 定价

- 每个结果 10 积分
- 缓存命中免费
- 相同查询 30 分钟内第二次调用免费

## ⚠️ 重要提示

### 性能

- `crawl_results=0`（默认）：0.5-2 秒
- `crawl_results=1-10`：每个结果增加 10-30 秒

### 成本

- 每个搜索结果：10 积分
- 缓存命中：免费（30 分钟内相同查询）
- **建议**：优先使用摘要，只在必要时抓取完整内容

### 最佳实践

1. **默认使用** `-n 3 -c 0`（快速获取摘要）
2. **只有用户明确要求"完整内容"时** 才设置 `-c > 0`
3. **搜索前** 先检查是否有缓存（相同查询 30 分钟内免费）
4. **合理控制数量** `max_results` 不要设置过大，避免不必要的成本

## 注意事项

1. 默认使用 `crawl_results=0` 以获得快速响应
2. 设置 `crawl_results > 0` 会显著增加延迟（10-30秒/页）
3. 注意控制请求频率，避免超出限流
4. 相同查询 30 分钟内会使用缓存，免费且更快

## 高级配置（可选）

如果需要使用自己的 API 服务，可以设置环境变量：

```bash
export SEARCH_API_KEY="your_api_key_here"
export SEARCH_API_BASE_URL="http://your-server:3000"
```

脚本会优先使用环境变量中的配置。
