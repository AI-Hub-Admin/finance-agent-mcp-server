# finance-agent-mcp-server
MCP Server of free and public available Financial Data without need of API keys from trusted sites or institues. 

[![MCP Marketplace User Review Rating Badge](https://www.deepnlp.org/api/marketplace/svg?name=ai-hub-admin/finance-agent-mcp-server)](https://www.deepnlp.org/store/mcp-server/mcp-server/pub-ai-hub-admin/finance-agent-mcp-server)

This MCP server is a mcp wrapper of pypi package FinanceAgent (https://github.com/AI-Hub-Admin/FinanceAgent) which aims to 
provide free and public available financial data from open websites of trusted sites. You can help your AI system to get realtime Financial Data From Global Market such US (NASDAQ/NYSE/DOW), China (HKEX, Shenzhen, Shanghai), Europe, India, Japan (TSE), etc.


# Features

1. Get Realtime Stock Price data from global market. Supports US (NASDAQ,NYSE,DOW) China (HKEX, SHANGHAI SH, SHENZHEN SZ) India (NSE) and London (LSE) of realtime 
crawling or API access to trusted sites, such as nasdaq.com,xueqiu.com,morningstar.com,marketbeat.com,etc.


**Supported source**

|  REGION  | MARKET| INVESTMENT TYPE | API DATA SOURCE   |
|  ----  | ----  | ----  | ----  | 
|  United Status  | US (NASDAQ,NYSE,DOW) | STOCK  | morningstar.com |
|  United Status  | US (NASDAQ,NYSE,DOW)  | STOCK  | zacks.com |
|  United Status  | US (NASDAQ,NYSE,DOW)  | STOCK  | marketbeat.com |
|  Asia  | HK (HKEX) | STOCK  | hkex.com |
|  Asia  | CN_MAINLAND (SHANGHAI SH, SHENZHEN SZ) | STOCK  | xueqiu.com |
|  Asia  | India (NSE) | STOCK  |  moneycontrol.com  |
|  Europe  | London (LSE) | STOCK  | stockanalysis.com |
|  Asia  | Toyko (TSE) | STOCK  | NA |



**Sample Output**

```

#### HK Stock Info
-----------------------------------
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
-----------------------------------
```


# Tools
get_stock_price_global_market(symbol_list: List[str], market: str) -> str:

## get_stock_price_global_market(symbol_list: List[str], market: str) -> str:

**Parameters**

-symbol_list: symbol_list (List): List of Symbols, such as Tencent: 700, Kuaishou: 1024, Tesla (TSLA), Microsoft(MSFT), Google (GOOG), London Stock Exchange Market, Shell (quote: SHEL), Unilever (quote: ULVR)

-market (str): "HK", "CN_MAINLAND", "US", "LSE", "NSE_INDIA", etc.


# MCP Integration
```
{
    "mcpServers": {
        "finance-agent-mcp-server": {
            "command": "uv",
            "args": ["--directory", "/path_to_folder/finance-agent-mcp-server/src/finance-agent-mcp-server", "run", "server.py"]
        }
    }
}
```

