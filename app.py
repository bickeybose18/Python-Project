

import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Advanced Dashboard", layout="wide")

# Dark UI
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🛍️ Product Pricing Dashboard")
st.markdown("### 📊 Interactive Data Visualization using Python")

# Load Data
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

# ------------------ Charts ------------------

# Bar Chart
st.subheader("💸 Price Comparison")

fig1 = px.bar(
    filtered_df.head(10),
    x='Product Name',
    y=['Old Price', 'Special Price'],
    barmode='group',
    title="Price Comparison",
)

st.plotly_chart(fig1, use_container_width=True)

# Pie Chart
st.subheader("🥧 Product Distribution")

pie_data = df['Product'].value_counts().head(5).reset_index()
pie_data.columns = ['Product', 'Count']

fig2 = px.pie(
    pie_data,
    names='Product',
    values='Count',
    title="Top 5 Product Categories",
)

st.plotly_chart(fig2, use_container_width=True)

# Line Chart
st.subheader("📈 Price Trend")

fig3 = px.line(
    filtered_df.head(10),
    y=['Old Price', 'Special Price'],
    title="Price Trend",
)

st.plotly_chart(fig3, use_container_width=True)

# Histogram
st.subheader("📉 Discount Distribution")

fig4 = px.histogram(
    df,
    x='Discount %',
    nbins=10,
    title="Discount Distribution",
)

st.plotly_chart(fig4, use_container_width=True)

# Top Products
st.subheader("🔥 Top Discounted Products")

top_products = df.sort_values(by='Discount %', ascending=False).head(10)
st.dataframe(top_products[['Product Name', 'Discount %']])

# Success Message
st.success("✅ Dashboard Successfully Deployed & Fully Interactive")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 👨‍💻 Project By  
    
    Bikas Kumar \n
    Anand Kumar \n
    Rajan Kumar singh \n
    
    """)

with col2:
    st.markdown("""
    ### 👨‍🏫 Guide By  
    **Mr. Harendra Kumar**
    """)
