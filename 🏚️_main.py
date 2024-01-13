import streamlit as st, pandas as pd, numpy as np, yfinance as yf, plotly.express as px

st.set_page_config(
    page_title="Stock Price Project",
    page_icon="🤖",
)

st.title("Stock Price Data Project")
st.sidebar.success("Select a page above.")
