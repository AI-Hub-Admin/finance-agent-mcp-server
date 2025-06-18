import asyncio  # Add asyncio import
import os
import sys
import time
import json

from typing import Deque, List, Optional, Tuple
from pydantic import BaseModel

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import Context, FastMCP

import FinanceAgent as fa
import logging

logging.basicConfig(
    filename='server.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

class CustomFastMCP(FastMCP):
    async def _handle_list_tools(self, context):
        # print(f"ListTools Request Details: {context.request}")
        context.info(f"ListTools _handle_list_tools Request Details: {context.request}")
        context.info(f"ListTools _handle_list_tools Request Details: {str(context.request)}")
        return await super()._handle_list_tools(context)

# Initialize FastMCP server
server = CustomFastMCP(
    "finance-agent-mcp-server",
    prompt="""
# Financial Agent MCP Server

This server provides tools to get realtime financial data from global financial market, such as stock market in NASDAQ,NYSE,DOW, HKEX, Shanghai,Shenzhen, LSE, TSE, NSE India, etc.

The API is free without need for keys, and the data sources are realtime crawling or public available APIs from websites such as nasdaq.com,morningstar.com,marketbeat.com, xueqiu.com, stockanalysis.com, etc. And the data from realtime fetched from website with proxy settings.

## Available Tools

### 1. get_stock_price_global_market

Use this tool to get realtime or near-realtime finance data is crucial for success of AI Agents, this tool can help build a common interface of open API to get public available data from global Finance Market (US, Europe, Asia) with multiple finance investment choices such as Stock, Index, Option, etc. 
Getting Realtime Data maybe blocked by website and this repo is not responsible for proxy or any data correctness related issues.


## Guidelines for Use

### Available Markets
REGION  MARKET  INVESTMENT TYPE API DATA SOURCE
United Status   US (NASDAQ,NYSE,DOW)    STOCK   morningstar.com
United Status   US (NASDAQ,NYSE,DOW)    STOCK   zacks.com
United Status   US (NASDAQ,NYSE,DOW)    STOCK   marketbeat.com
Asia    HK (HKEX)   STOCK   hkex.com
Asia    CN_MAINLAND (SHANGHAI SH, SHENZHEN SZ)  STOCK   xueqiu.com
Asia    India (NSE) STOCK   moneycontrol.com
Europe  London (LSE)    STOCK   stockanalysis.com
Asia    Toyko (TSE) STOCK   NA

## Output Format
#### HK Stock Info
---------
symbol|1024
avg_price|49.650 HKD
high|50.950 HKD
low|47.600 HKD
previous_close|50.850 HKD
update_time|14 Oct 2024 18:33
market_capitalization|214.06 B HKD
pe_ratio|31.15
source|HKEX, https://www.hkex.com.hk/Market-Data/Securities-Prices/Equities/Equities-Quote?sym=1024&sc_lang=en
data_source|hkex.com

""",
)

@server.tool()
def get_stock_price_global_market(
        symbol_list: List[str], market: str
    ) -> str:
    """ Get Public Available Stock Symbols from Global Marketplace

        Args:
            symbol_list (List): List of Symbols, such as Tencent: 700, Kuaishou: 1024, Tesla (TSLA), Microsoft(MSFT), Google (GOOG), London Stock Exchange Market, Shell (quote: SHEL), Unilever (quote: ULVR)
            market (str): "HK", "CN_MAINLAND", "US", "LSE", "NSE_INDIA", etc.
        
        Return: 
            str: json str with below values samples

            [{'symbol': 'SH600036',
              'current': 45.78,
              'percent': 1.33,
              'chg': 0.6,
              'high': '45.81 CNY',
              'low': '44.95 CNY',
              'avg_price': '45.485751910823915 CNY',
              'timestamp': 1750057200000,
              'open': 45.08,
              'last_close': 45.18,
              'market_capital': 1154564531614.0,
              'change': '0.6(1.33%)',
              'previous_close': '45.18 CNY',
              'market_capitalization': '11545.65 亿 CNY',
              'pe_ratio': '',
              'update_time': '2025-06-16 15:00:00',
              'source': 'XUEQIU.COM, https://xueqiu.com/S/SH600036',
              'data_source': 'xueqiu.com',
              'source_url': 'https://xueqiu.com/S/SH600036'},
    """
    try:
        # results list of json
        results = fa.api(symbol_list=symbol_list, market=market)            
        output = json.dumps(results)    
        return output

    except httpx.HTTPError as e:
        return f"Error communicating with FinanceAgent API: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

if __name__ == "__main__":
    # Initialize and run the server
    server.run(transport='stdio')
    # server.run(transport="sse", port=6278)
