# Stock Profit Opportunities Dashboard

This project is a Python-based dashboard that analyzes stock price data for a collection of companies and identifies profit opportunities based on the calculated ratios. It provides visualizations and rankings of the profit opportunities to aid in investment decision-making.

1. Update the company_data list in the code below with the companies you want to analyze. Each company should be represented as a dictionary with the keys 'name' and 'multiplier', where 'name' is the ticker symbol and 'multiplier' is the scaling factor.

```python
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import itertools

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
one_month_ago = (pd.Timestamp.today() - pd.DateOffset(months=1)).strftime('%Y-%m-%d')
now = pd.Timestamp.today().strftime('%Y-%m-%d')

# Set initial fx rate
fx_rate = 100

# Fetch data for a single company
def fetch_data(company):
    # ...

# Fetch data for the given companies in parallel
def fetch_data_parallel(companies, start_date, end_date):
    # ...

# Calculate ratios based on the fetched data
def calculate_ratios(data_dict):
    # ...

# Calculate profit opportunities based on the ratios
def calculate_profit(ratios_dict, fx_rate):
    # ...

# Create a line plot to visualize the ratios of each company over time
def line_plot_ratios(data_dict):
    # ...

# Create a scatter plot to visualize the profit opportunities
def scatter_plot_profit(profit_dict):
    # ...

# Create a heatmap to visualize the profit opportunities
def heatmap_profit(profit_dict):
    # ...

# Fetch data, calculate ratios, and calculate profit in parallel
data_dict = fetch_data_parallel(company_data, one_month_ago, now)
ratios_dict = calculate_ratios(data_dict)
profit_dict = calculate_profit(ratios_dict, fx_rate)

# Create visualizations
line_plot_ratios(data_dict)
scatter_plot_profit(profit_dict)
heatmap_profit(profit_dict)
```

Run the Python script and observe the generated visualizations.