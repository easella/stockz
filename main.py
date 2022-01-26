import streamlit as st
from datetime import date
import yfinance as yf
import fbprophet as Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objects as go
START="2015-01-01"
TODAY=date.today().strftime("%Y-%m-%d")
st.title("stock prediction app")
stocks=("NET","BRN.AX","GME","GOOG")
selected_stocks=st.selectbox("Select dataset for prediction",stocks)
n_years=st.slider("Years od prediction:",1,4)
preiod=n_years*365

