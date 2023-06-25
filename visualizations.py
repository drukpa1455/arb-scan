import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Dict

def line_plot_ratios(data_dict: Dict[str, pd.DataFrame]) -> None:
    st.subheader("Line Plot of Ratios")

    for company, data in data_dict.items():
        st.write(f"Company: {company}")

        if not data.empty and 'Ratio' in data.columns:
            # Plot line chart
            fig, ax = plt.subplots()
            sns.lineplot(data=data.reset_index(), x="Date", y="Ratio")
            plt.xlabel("Date")
            plt.ylabel("Ratio")
            plt.title(f"Ratio of {company}")
            st.pyplot(fig)
        else:
            st.write("Data is empty or does not contain the 'Ratio' column for this company. Skipping the plot.")

from pandas import DataFrame

def scatter_plot_profit(profit_dict: Dict[str, pd.DataFrame]) -> None:
    st.subheader("Scatter Plot of Profit")
    
    for company, data in profit_dict.items():
        st.write(f"Company: {company}")
        
        if not isinstance(data, DataFrame):
            st.write(f"Data for {company} is not a DataFrame. Skipping this plot.")
            continue

        # Check if "Days Held" and "Profit" are in data columns
        if not ('Days Held' in data.columns and 'Profit' in data.columns):
            st.write(f"Data for {company} does not contain 'Days Held' or 'Profit' column. Skipping this plot.")
            continue

        # Plot scatter chart
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x="Days Held", y="Profit", hue="Buy/Sell")
        plt.xlabel("Days Held")
        plt.ylabel("Profit")
        plt.title(f"Profit of {company}")
        st.pyplot(fig)

def heatmap_profit(profit_dict: Dict[str, pd.DataFrame]) -> None:
    st.subheader("Heatmap of Profit")
    
    for company, data in profit_dict.items():
        st.write(f"Company: {company}")
        
        # Plot heatmap
        fig, ax = plt.subplots()
        data_pivot = data.pivot(index="Days Held", columns="Buy/Sell", values="Profit")
        sns.heatmap(data_pivot, annot=True, fmt=".2f", cmap="RdYlGn_r")
        plt.xlabel("Buy/Sell")
        plt.ylabel("Days Held")
        plt.title(f"Profit Heatmap of {company}")
        st.pyplot(fig)
