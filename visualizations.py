import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
import pandas as pd

def line_plot_ratios(data_dict: Dict[str, pd.DataFrame]) -> None:
    """
    Create line plots of the ratios over time for each company.

    Parameters:
    - data_dict (dict): A dictionary containing the fetched data for each company.

    Returns:
    - None
    """
    st.subheader("Ratios Over Time")
    sns.set(style="darkgrid")
    for company, data in data_dict.items():
        st.write(f"## Ratio Over Time for {company}")
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=data, x=data.index, y=f"Ratio_{company}")
        plt.xlabel("Date")
        plt.ylabel("Ratio")
        plt.xticks(rotation=45)
        st.pyplot()

def scatter_plot_profit(profit_dict: Dict[str, List[Tuple[int, int, float]]]) -> None:
    """
    Create a scatter plot of the profit opportunities.

    Parameters:
    - profit_dict (dict): A dictionary containing the profit opportunities for each combination of companies.

    Returns:
    - None
    """
    st.subheader("Profit Opportunities")
    plt.figure(figsize=(12, 6))
    for combination, opportunities in profit_dict.items():
        x = [opportunity[0] for opportunity in opportunities]
        y = [opportunity[1] for opportunity in opportunities]
        z = [opportunity[2] for opportunity in opportunities]
        plt.scatter(x, y, c=z, cmap='coolwarm', alpha=0.7)
    plt.colorbar(label='Profit')
    plt.xlabel('Buy Index')
    plt.ylabel('Sell Index')
    plt.xticks(list(range(len(data_dict))), list(data_dict.keys()), rotation=45)
    st.pyplot()

def heatmap_profit(profit_dict: Dict[str, List[Tuple[int, int, float]]]) -> None:
    """
    Create a heatmap of the profit opportunities.

    Parameters:
    - profit_dict (dict): A dictionary containing the profit opportunities for each combination of companies.

    Returns:
    - None
    """
    st.subheader("Profit Opportunities Heatmap")
    max_profit = max([opportunity[2] for opportunities in profit_dict.values() for opportunity in opportunities])
    profit_matrix = []
    for i, combination in enumerate(profit_dict.keys()):
        opportunities = profit_dict[combination]
        row = [opportunity[2] if opportunity[2] > 0 else 0 for opportunity in opportunities]
        row += [0] * (len(data_dict) - len(opportunities))
        profit_matrix.append(row)
    plt.figure(figsize=(12, 8))
    sns.heatmap(profit_matrix, cmap='coolwarm', cbar=True, annot=True, vmin=0, vmax=max_profit, fmt=".2f",
                xticklabels=list(data_dict.keys()), yticklabels=list(profit_dict.keys()))
    plt.xlabel('Companies')
    plt.ylabel('Combinations')
    plt.xticks(rotation=45)
    st.pyplot()
