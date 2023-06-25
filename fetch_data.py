import yfinance as yf
import pandas as pd
from typing import Dict, List

def fetch_data_parallel(companies: List[Dict[str, any]], start_date: str, end_date: str) -> Dict[str, pd.DataFrame]:
    data_dict = {}

    for company in companies:
        ticker_ADR = yf.Ticker(company['name'])
        ticker_local = yf.Ticker(f"{company['name']}.BA")

        try:
            data_ADR = ticker_ADR.history(start=start_date, end=end_date)
            data_local = ticker_local.history(start=start_date, end=end_date)

            if data_ADR.empty or data_local.empty:
                print(f"Data for {company['name']} or {company['name']}.BA is empty. Skipping this ticker.")
                continue

            data_ADR = data_ADR.rename(columns={'Close': f'Close_{company["name"]}'})
            data_local = data_local.rename(columns={'Close': f'Close_{company["name"]}.BA'})
            data = pd.concat([data_ADR[f'Close_{company["name"]}'], data_local[f'Close_{company["name"]}.BA']], axis=1)

            data[f'Ratio_{company["name"]}'] = (data[f'Close_{company["name"]}.BA'] / data[f'Close_{company["name"]}']) * company["multiplier"]
            data_dict[company['name']] = data

        except Exception as e:
            print(f"Failed to fetch data for {company['name']} or {company['name']}.BA:", e)

    return data_dict
