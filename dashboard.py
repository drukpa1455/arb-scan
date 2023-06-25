import pandas as pd
import yfinance as yf
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from typing import Dict, List, Optional

def fetch_data(company: Dict[str, any], start_date: str, end_date: str) -> Optional[pd.DataFrame]:
    """
    Fetches stock price data for a single company.

    Parameters:
    - company (dict): A dictionary representing the company with 'name' and 'multiplier' keys.
    - start_date (str): The start date in the format 'YYYY-MM-DD'.
    - end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
    - data (DataFrame): The fetched data for the company, or None if data is empty.
    """
    data_ADR = yf.download(company['name'], start=start_date, end=end_date)
    data_local = yf.download(company['name'] + ".BA", start=start_date, end=end_date)

    if data_ADR.empty or data_local.empty:
        return None

    data_ADR = data_ADR.rename(columns={'Close': 'Close_' + company['name']})
    data_local = data_local.rename(columns={'Close': 'Close_' + company['name'] + '.BA'})
    data = pd.concat([data_ADR['Close_' + company['name']], data_local['Close_' + company['name'] + '.BA']], axis=1)

    data['Ratio_' + company['name']] = (data['Close_' + company['name'] + '.BA'] / data['Close_' + company['name']]) * company['multiplier']

    return data

def fetch_data_parallel(companies: List[Dict[str, any]], start_date: str, end_date: str) -> Dict[str, pd.DataFrame]:
    """
    Fetches stock price data for the given companies in parallel.

    Parameters:
    - companies (list): A list of dictionaries representing the companies with 'name' and 'multiplier' keys.
    - start_date (str): The start date in the format 'YYYY-MM-DD'.
    - end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
    - data_dict (dict): A dictionary containing the fetched data for each company.
    """
    data_dict = {}

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(fetch_data, company, start_date, end_date) for company in companies]

        with tqdm(total=len(futures), desc="Fetching data") as pbar:
            for future in as_completed(futures):
                data = future.result()
                if data is not None:
                    data_dict[data.columns[0].split('_')[-1]] = data
                pbar.update()

    return data_dict