import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Data Exploration')

# User Inputs
start_date = st.date_input('Start Date', value=pd.to_datetime('2021-01-01'))
end_date = st.date_input('End Date', value=pd.to_datetime('2022-01-01'))

company_name = st.text_input('Company Name', value='CompanyA')

# Dummy Data Creation
date_range = pd.date_range(start=start_date, end=end_date)
df = pd.DataFrame({"Date": date_range, 
                   "Company": [company_name for _ in range(len(date_range))],
                   "Ratio": pd.np.random.rand(len(date_range)),
                   "Profit": pd.np.random.rand(len(date_range)) * 100,
                   "Days Held": pd.np.random.randint(1, 100, len(date_range)),
                   "Buy/Sell": pd.np.random.choice(["Buy", "Sell"], len(date_range))})

# Line plot
st.subheader("Line Plot of Ratios")
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Date", y="Ratio")
plt.xlabel("Date")
plt.ylabel("Ratio")
plt.title(f"Ratio of {company_name}")
st.pyplot(fig)

# Scatter Plot
st.subheader("Scatter Plot of Profit")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="Days Held", y="Profit", hue="Buy/Sell")
plt.xlabel("Days Held")
plt.ylabel("Profit")
plt.title(f"Profit of {company_name}")
st.pyplot(fig)

# Heatmap
st.subheader("Heatmap of Profit")
df_grouped = df.groupby(["Days Held", "Buy/Sell"])["Profit"].mean().reset_index()
data_pivot = df_grouped.pivot(index="Days Held", columns="Buy/Sell", values="Profit")
fig, ax = plt.subplots()
sns.heatmap(data_pivot, annot=True, fmt=".2f", cmap="RdYlGn_r")
plt.xlabel("Buy/Sell")
plt.ylabel("Days Held")
plt.title(f"Profit Heatmap of {company_name}")
st.pyplot(fig)
