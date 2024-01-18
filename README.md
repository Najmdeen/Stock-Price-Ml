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
