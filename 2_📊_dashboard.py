import streamlit as st, pandas as pd, numpy as np, yfinance as yf, plotly.express as px
from stocknews import StockNews
from alpha_vantage.fundamentaldata import FundamentalData

st.title("Stock Dashboard")

ticker = st.sidebar.text_input("Input Stock Ticker")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")


@st.cache
def load_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data


def plot_stock(data, column: str):
    fig = px.line(data, x=data.index, y=data[column], title=ticker)
    st.plotly_chart(fig)


if ticker:
    data = load_data(ticker=ticker)
    st.subheader(ticker)

    column_name = st.sidebar.selectbox("Select Plot Colum", data.columns)

    plot_stock(data, column_name)

    raw_data, fundamental_data, news = st.tabs(["Raw Data", "Fundamental Data", "News"])

    with raw_data:
        st.write("Raw")
        data2 = data.copy()
        data2["% Change"] = data2["Adj Close"] / data["Adj Close"].shift(1) - 1
        st.write(data2)
        annual_return = data2["% Change"].mean() * 252 * 100
        stdev = (np.std(data2["% Change"]) * np.sqrt(252)) * 100
        st.write("Annual Return is: ", annual_return, "%")
        st.write("Standard Deviation is: ", stdev, "%")
        st.write("Risk Adj Return is: ", annual_return / stdev, "%")

    with news:
        st.header(f"News of  {ticker}")
        sn = StockNews(ticker, save_news=False)
        df_news = sn.read_rss()
        for i in range(7):
            st.subheader(f"News {i+1}")
            st.write(df_news["published"][i])
            st.write(df_news["title"][i])
            st.write(df_news["summary"][i])
            title_sentiment = df_news["sentiment_title"][i]
            news_sentiment = df_news["sentiment_summary"][i]
            st.write(f"Title Sentiment {title_sentiment}")
            st.write(f"New Sentiment {news_sentiment}")

    with fundamental_data:
        key = "XKZB93V9YJWSLOK3"
        fd = FundamentalData(key, output_format="pandas")
        # Balance sheet
        st.subheader("Balance Sheet")
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
        # Income Statement
        st.subheader("Income Statement")
        income_statement = fd.get_income_statement_annual(ticker)[0]
        ist = income_statement.T[2:]
        ist.columns = list(income_statement.T.iloc[0])
        st.write(ist)
        st.subheader("Cash Flow Statement")
        cash_flow = fd.get_cash_flow_annual(ticker)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)
