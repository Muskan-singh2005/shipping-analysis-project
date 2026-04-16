import streamlit as st
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Shipping Analytics Dashboard",
    layout="wide"
)

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("data/processed_data.csv")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔍 Filters")

region = st.sidebar.selectbox("Select Region", ["All"] + list(df['Region'].unique()))
ship_mode = st.sidebar.selectbox("Select Ship Mode", ["All"] + list(df['Ship Mode'].unique()))

# Apply filters
filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df['Region'] == region]

if ship_mode != "All":
    filtered_df = filtered_df[filtered_df['Ship Mode'] == ship_mode]

# -------------------------------
# Title
# -------------------------------
st.title("🚚 Shipping Route Efficiency Dashboard")

# -------------------------------
# KPIs
# -------------------------------
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", len(filtered_df))
col2.metric("Avg Lead Time", round(filtered_df['Lead Time'].mean(), 2))
col3.metric("Max Lead Time", filtered_df['Lead Time'].max())
col4.metric("Min Lead Time", filtered_df['Lead Time'].min())

# -------------------------------
# Route Analysis
# -------------------------------
st.subheader("🛣️ Route Efficiency Analysis")

route = filtered_df.groupby('Route')['Lead Time'].mean().reset_index()
route = route.sort_values('Lead Time')

st.bar_chart(route.set_index('Route'))

# -------------------------------
# Top & Worst Routes
# -------------------------------
col1, col2 = st.columns(2)

top_routes = route.head(10)
worst_routes = route.tail(10)

with col1:
    st.markdown("### 🔥 Top 10 Fastest Routes")
    st.dataframe(top_routes)

with col2:
    st.markdown("### 🚨 Top 10 Slowest Routes")
    st.dataframe(worst_routes)

# -------------------------------
# Ship Mode Comparison
# -------------------------------
st.subheader("🚀 Ship Mode Performance")

ship_mode_df = filtered_df.groupby('Ship Mode')['Lead Time'].mean()
st.bar_chart(ship_mode_df)

# -------------------------------
# Region Analysis
# -------------------------------
st.subheader("🌍 Region-wise Performance")

region_df = filtered_df.groupby('Region')['Lead Time'].mean()
st.bar_chart(region_df)

# -------------------------------
# Raw Data
# -------------------------------
st.subheader("📂 Data Preview")
st.dataframe(filtered_df.head(100))