# Stock Price Project

## Introduction
The "Stock Price Project" is an interactive web application designed for stock market enthusiasts and investors. This application features a Streamlit-based homepage and two sub-pages, offering both a stock price dashboard and a stock price prediction tool using Facebook Prophet.

## Features
- **Stock Price Dashboard:** Allows users to view and analyze historical stock prices.
- **Stock Price Prediction:** Utilizes Facebook Prophet for forecasting future stock prices.

## Installation
Before running the project, ensure you have the following modules installed:
```python
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from stocknews import StockNews
from alpha_vantage.fundamentaldata import FundamentalData
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
```


## Usage
To run the application, navigate to the project directory and execute:
```shell
streamlit run app.py
```
## Main Page
The main page sets up the Streamlit configuration and presents the project title and navigation options.
```python
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

# Streamlit page configuration
st.set_page_config(page_title="Stock Price Project", page_icon="🤖")

# Main title
st.title("Stock Price Data Project")
st.sidebar.success("Select a page above.")
```
## Dashboard Page
This page allows users to input a stock ticker, select a date range, and view the stock's performance.
```python
# Imports and page setup (omitted for brevity)

# Dashboard title
st.title("Stock Dashboard")

# User input for stock ticker and date range
ticker = st.sidebar.text_input("Input Stock Ticker")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Function definitions and data visualization (omitted for brevity)
```

## Prediction Page
Offers stock price prediction using Facebook Prophet.
```python
# Imports and page setup (omitted for brevity)

st.title("Price Prediction ML")

# User input and data preparation (omitted for brevity)

# Prediction and visualization (omitted for brevity)
```
## Contributing
Contributions to the "Stock Price Project" are welcome. If you have suggestions or improvements, please fork the repository and submit a pull request.
