import streamlit as st
from fetch_data import fetch_data_parallel
from calculate_ratios import calculate_ratios
from calculate_profit import calculate_profit
from visualizations import line_plot_ratios, scatter_plot_profit, heatmap_profit
from typing import Dict, List, Tuple

def create_web_dashboard(company_data: List[Dict[str, any]], start_date: str, end_date: str, fx_rate: float) -> None:
    # Fetch data
    data_dict = fetch_data_parallel(company_data, start_date, end_date)

    # Calculate ratios
    ratios_dict = calculate_ratios(data_dict)

    # Calculate profit
    profit_dict = calculate_profit(ratios_dict, fx_rate)

    # Visualizations
    line_plot_ratios(data_dict)
    scatter_plot_profit(profit_dict)
    heatmap_profit(profit_dict)

def main():
    st.set_page_config(page_title="Arbitrage Scanner", layout="wide")

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
    start_date = '2023-06-01'
    end_date = '2023-06-30'

    # Set initial FX rate
    fx_rate = 100

    # Create the web dashboard
    create_web_dashboard(company_data, start_date, end_date, fx_rate)

if __name__ == '__main__':
    main()
