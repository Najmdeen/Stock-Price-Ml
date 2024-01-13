import streamlit as st
import yfinance as yf
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go


st.title("Price Prediction ML")
START = "2018-01-01"

TODAY = date.today().strftime("%Y-%m-%d")

# stock = ("TSLA", "AAPL", "AMZN", "NVDA", "MSFT")
ticker = st.sidebar.text_input("Input Stock Ticker")

# selected_stock = st.selectbox("Select a NASDAQ Stock Symbol", stock)

n_years = st.slider("Years of prediction ", 1, 5)
period = n_years * 365  # yrs in days


st.write("The project is about the prediction of stock price using facebook prophet")


@st.cache_data
def get_data(ticker):
    df = yf.download(ticker, START, TODAY)
    df.reset_index(inplace=True)
    return df


# Visualize data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock_open"))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock_close"))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


if ticker:
    data = get_data(ticker=ticker)
    # Print data
    st.header("Raw Data")
    st.write(data.tail())

    plot_raw_data()

    # Rename features for forcasting
    df = data[["Date", "Close"]]
    df = df.rename(columns={"Date": "ds", "Close": "y"})

    # Forecasting
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=period)
    forecast = model.predict(future)

    # Print forecast
    st.header("Forecast Data")
    st.write(forecast.tail())

    fig1 = plot_plotly(model, forecast)
    st.plotly_chart(fig1)

    st.write("forecast Components")
    fig2 = model.plot_components(forecast)

    st.write(fig2)
