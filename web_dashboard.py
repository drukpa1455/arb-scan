import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
    st.title('Stock Profit Opportunities Dashboard')

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
    
    companies = [company['name'] for company in company_data]
    selected_companies = st.multiselect('Select companies', companies, default=companies)

    company_data = [company for company in company_data if company['name'] in selected_companies]

    # Select start and end dates
    start_date = st.date_input("Start date", value=pd.to_datetime('2023-01-01'))
    end_date = st.date_input("End date", value=pd.to_datetime('2023-01-31'))

    # Select fx rate
    fx_rate = st.slider('Select FX rate', min_value=1.0, max_value=200.0, value=100.0)

    # Create the dashboard
    create_dashboard(company_data, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), fx_rate)

if __name__ == '__main__':
    main()
