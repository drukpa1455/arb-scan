"""
Stock Profit Opportunities Dashboard

This script fetches stock price data for a collection of companies, calculates profit opportunities based on the ratios, and visualizes the data through various plots.

The main steps involved in the dashboard are:
1. Fetching data for each company from Yahoo Finance.
2. Calculating the ratios based on the fetched data.
3. Identifying profit opportunities by comparing the ratios.
4. Creating visualizations to analyze and explore the profit opportunities.

Dependencies:
- pandas
- yfinance
- seaborn
- matplotlib
- tqdm

"""

from fetch_data import fetch_data_parallel
from calculate_profit import calculate_profit
from visualizations import line_plot_ratios, scatter_plot_profit, heatmap_profit
from typing import List, Dict, Any

def create_dashboard(company_data: List[Dict[str, Any]], start_date: str, end_date: str, fx_rate: float) -> None:
    """
    Creates a stock profit opportunities dashboard.

    Parameters:
    - company_data (list): A list of dictionaries representing the companies with 'name' and 'multiplier' keys.
    - start_date (str): The start date in the format 'YYYY-MM-DD'.
    - end_date (str): The end date in the format 'YYYY-MM-DD'.
    - fx_rate (float): The exchange rate.

    Returns:
    - None
    """

    # Fetch data in parallel
    data_dict = fetch_data_parallel(company_data, start_date, end_date)

    # Calculate ratios
    ratios_dict = {}
    for company, data in data_dict.items():
        ratios_dict[company] = data['Ratio_' + company]

    # Calculate profit opportunities
    profit_dict = calculate_profit(ratios_dict, fx_rate)

    # Create visualizations
    line_plot_ratios(data_dict)
    scatter_plot_profit(profit_dict)
    heatmap_profit(profit_dict)

def main() -> None:
    """
    Main function to execute the stock profit opportunities dashboard.
    """

    # Define list of companies and their multipliers
    company_data = [
        {'name': 'CEPU', 'multiplier': 10},
        {'name': 'CRESY', 'multiplier': 1},
        {'name': 'EDN', 'multiplier': 20},
        {'name': 'GGAL', 'multiplier': 10},
        {'name': 'SUPV', 'multiplier': 5},
        {'name': 'IRS', 'multiplier': 10},
        {'name': 'LOMA', 'multiplier': 5},
        {'name': 'PAM', 'multiplier': 25},
        {'name': 'TEO', 'multiplier': 5},
        {'name': 'TS', 'multiplier': 1},
        {'name': 'TX', 'multiplier': 1},
        {'name': 'TGS', 'multiplier': 1},
    ]

    # Define start and end dates
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    # Set initial fx rate
    fx_rate = 100

    # Create the dashboard
    create_dashboard(company_data, start_date, end_date, fx_rate)

if __name__ == '__main__':
    main()
