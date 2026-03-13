#!/usr/bin/env python3
"""
Search API 调用的封装脚本
支持通用搜索和新闻搜索
"""

import argparse
import json
import os
import requests
import sys
import time
import io

# 解决中文编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# API 配置
BASE_URL = os.getenv('SEARCH_API_BASE_URL', 'http://localhost:3000')
API_KEY = os.getenv('SEARCH_API_KEY')

if not API_KEY:
    print("错误: 请设置 SEARCH_API_KEY 环境变量", file=sys.stderr)
    print("示例: export SEARCH_API_KEY='your_api_key_here'", file=sys.stderr)
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def check_service_status():
    """检查 API 服务是否可用"""
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        return True
    except requests.exceptions.RequestException:
        return False

def search(query, search_service="baidu", max_results=3, crawl_results=0):
    """通用搜索"""
    payload = {
        "query": query,
        "search_service": search_service,
        "max_results": max_results,
        "crawl_results": crawl_results
    }

    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/search",
            headers=HEADERS,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": f"无法连接到 {BASE_URL}，请确认 Search API 服务已启动"
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "请求超时，如果设置了 crawl_results > 0，请耐心等待或减少该值"
        }
    except requests.exceptions.HTTPError as e:
        return {
            "success": False,
            "error": f"HTTP 错误 {response.status_code}: {response.text}"
        }
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "API 返回了无效的 JSON 响应"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"未知错误: {str(e)}"
        }

def news(query, search_service="google", max_results=3, crawl_results=0):
    """新闻搜索"""
    payload = {
        "query": query,
        "search_service": search_service,
        "max_results": max_results,
        "crawl_results": crawl_results
    }

    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/news",
            headers=HEADERS,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": f"无法连接到 {BASE_URL}，请确认 Search API 服务已启动"
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "请求超时，如果设置了 crawl_results > 0，请耐心等待或减少该值"
        }
    except requests.exceptions.HTTPError as e:
        return {
            "success": False,
            "error": f"HTTP 错误 {response.status_code}: {response.text}"
        }
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "API 返回了无效的 JSON 响应"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"未知错误: {str(e)}"
        }

def main():
    parser = argparse.ArgumentParser(description="Search API Client")
    parser.add_argument("type", choices=["search", "news"], help="搜索类型: search 或 news")
    parser.add_argument("query", help="搜索关键词")
    parser.add_argument("-s", "--service", default="baidu", help="搜索服务 (search: baidu/google/bing/duckduckgo/yahoo/wechat/youtube/github/reddit/bilibili, news: google/bing/duckduckgo/yahoo)")
    parser.add_argument("-n", "--max-results", type=int, default=3, help="返回结果数量 (1-20, 默认3)")
    parser.add_argument("-c", "--crawl-results", type=int, default=0, help="爬取完整内容的结果数 (0-10, 默认0,仅在需要时设置)")

    args = parser.parse_args()

    # 参数验证
    if not (1 <= args.max_results <= 20):
        parser.error("max_results 必须在 1-20 之间")
    if not (0 <= args.crawl_results <= 10):
        parser.error("crawl_results 必须在 0-10 之间")

    # 检查服务状态
    if not check_service_status():
        print(f"警告: 无法连接到 {BASE_URL}，请确认 Search API 服务已启动", file=sys.stderr)
        print(f"提示: 请在另一个终端启动服务，或检查 SEARCH_API_BASE_URL 环境变量", file=sys.stderr)
        return 1

    if args.type == "search":
        result = search(args.query, args.service, args.max_results, args.crawl_results)
    else:
        result = news(args.query, args.service, args.max_results, args.crawl_results)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 检查返回结果
    if result.get("success"):
        return 0
    else:
        print(f"Error: {result.get('error', 'Unknown error')}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
