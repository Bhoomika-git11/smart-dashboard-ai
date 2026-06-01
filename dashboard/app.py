import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Smart AI Dashboard", layout="wide")

st.title("📊 Smart Dashboard with Automated Insights")

df = pd.read_csv("smart-dashboard-ai/data/sample_sales.csv")
st.subheader("📈 Sales Data")
st.dataframe(df)

st.subheader("📊 Sales by Region")
st.bar_chart(df.groupby("region")["sales"].sum())

if st.button("Generate AI Insights"):
    response = requests.get("http://localhost:8000/analyze")
    result = response.json()

    st.subheader("🤖 AI Generated Insight")
    st.success(result["ai_insight"])
