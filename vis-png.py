import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
import pandas as pd

def line_plot_ratios(data_dict: Dict[str, pd.DataFrame]) -> None:
    """
    Creates a line plot to visualize the ratios of each company over time.

    Parameters:
    - data_dict (dict): A dictionary containing the fetched data for each company.
    """
    plt.figure(figsize=(12, 6))
    for company, data in data_dict.items():
        sns.lineplot(data=data, x=data.index, y='Ratio_' + company, label=company)
    plt.xlabel('Date')
    plt.ylabel('Ratio')
    plt.title('Ratios Over Time')
    plt.legend()
    plt.show()

def scatter_plot_profit(profit_dict: Dict[str, List[Tuple[int, int, float]]]) -> None:
    """
    Creates a scatter plot to visualize the profit opportunities.

    Parameters:
    - profit_dict (dict): A dictionary containing the profit opportunities for each combination of companies.
    """
    plt.figure(figsize=(8, 6))
    for combination, profit_opportunities in profit_dict.items():
        buy_indices = [opportunity[0] for opportunity in profit_opportunities]
        sell_indices = [opportunity[1] for opportunity in profit_opportunities]
        profits = [opportunity[2] for opportunity in profit_opportunities]
        plt.scatter(buy_indices, sell_indices, c=profits, cmap='coolwarm', alpha=0.7)
    plt.colorbar(label='Profit')
    plt.xlabel('Buy Index')
    plt.ylabel('Sell Index')
    plt.title('Profit Opportunities')
    plt.grid(True)
    plt.show()

def heatmap_profit(profit_dict: Dict[str, List[Tuple[int, int, float]]]) -> None:
    """
    Creates a heatmap to visualize the profit opportunities.

    Parameters:
    - profit_dict (dict): A dictionary containing the profit opportunities for each combination of companies.
    """
    profit_matrix = []
    companies = list(profit_dict.keys())
    for combination, profit_opportunities in profit_dict.items():
        profits = [opportunity[2] for opportunity in profit_opportunities]
        profit_matrix.append(profits)

    plt.figure(figsize=(8, 6))
    sns.heatmap(profit_matrix, cmap='coolwarm', annot=True, fmt='.2f', xticklabels=companies, yticklabels=companies)
    plt.xlabel('Company 2')
    plt.ylabel('Company 1')
    plt.title('Profit Opportunities Heatmap')
    plt.show()
