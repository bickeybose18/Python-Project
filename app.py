import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Advanced Dashboard", layout="wide")

st.title("🛍️ Product Pricing Dashboard")

# Load data
df = pd.read_csv("Sports_ECommerce_Products_Data.csv")

# Data Cleaning
df['Old Price'] = pd.to_numeric(df['Old Price'], errors='coerce')
df['Special Price'] = pd.to_numeric(df['Special Price'], errors='coerce')
df['Discount %'] = pd.to_numeric(df['Discount %'], errors='coerce')
df.dropna(inplace=True)

# Sidebar Filter
st.sidebar.header("🔍 Filters")
category = st.sidebar.selectbox("Select Category", df['Product'].unique())

filtered_df = df[df['Product'] == category]

# KPI Cards
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Avg Old Price", int(filtered_df['Old Price'].mean()))
col2.metric("Avg Special Price", int(filtered_df['Special Price'].mean()))
col3.metric("Max Discount (%)", int(filtered_df['Discount %'].max()))

# Layout
col1, col2 = st.columns(2)

# Bar Chart
with col1:
    st.subheader("💸 Price Comparison")
    fig, ax = plt.subplots()
    filtered_df[['Old Price', 'Special Price']].head(10).plot(kind='bar', ax=ax)
    st.pyplot(fig)

pie_data = df['Product'].value_counts().head(5)

fig2, ax2 = plt.subplots()

# Pie without labels
wedges, texts, autotexts = ax2.pie(
    pie_data,
    autopct='%1.1f%%',
    startangle=90
)

# Legend outside (clean look)
ax2.legend(
    wedges,
    pie_data.index,
    title="Products",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

st.pyplot(fig2)

# Histogram
st.subheader("📉 Discount Distribution")
fig4, ax4 = plt.subplots()
sns.histplot(df['Discount %'], bins=10, ax=ax4)
st.pyplot(fig4)

# Top Products
st.subheader("🔥 Top Discounted Products")
top_products = df.sort_values(by='Discount %', ascending=False).head(10)
st.write(top_products[['Product Name', 'Discount %']])
