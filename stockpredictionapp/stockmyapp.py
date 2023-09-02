import yfinance as yf
import streamlit as st
import pandas as pd

st.write (""" Simple Stock Price App""")

tickersymbol = "GOOGL"

tickerData = yf.Ticker(tickersymbol)

tickerDF= tickerData.history(period="1d",start="2012-5-31",end="2020-5-31")

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)