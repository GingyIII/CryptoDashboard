import yfinance as yf  # yahoofinance
import streamlit as st
from PIL import Image
from urllib.request import urlopen

# Titles/subtitles
st.title("Cryptocurrency Daily Prices")
st.header("Main Dashboard")

# ticker vars
Bitcoin = 'BTC-USD'
Etheruem = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = 'BCH-USD'
Tether = 'USDT-USD'
Solana = 'SOL-USD'


# access data from yahoo finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Etheruem)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)
USDT_Data = yf.Ticker(Tether)
SOL_Data = yf.Ticker(Solana)


# fetch hist data from yfinance
BTC_His = BTC_Data.history(period="max")
ETH_His = ETH_Data.history(period="max")
XRP_His = XRP_Data.history(period="max")
BCH_His = BCH_Data.history(period="max")
USDT_His = USDT_Data.history(period="max")
SOL_His = SOL_Data.history(period="max")


# fetch crypto data for the dataframe
BTC = yf.download(Bitcoin, start="2022-2-26", end="2022-2-26")
ETH = yf.download(Etheruem, start="2022-2-26", end="2022-2-26")
XRP = yf.download(Ripple, start="2022-2-26", end="2022-2-26")
BCH = yf.download(BitcoinCash, start="2022-2-26", end="2022-2-26")
USDT = yf.download(Tether, start="2022-2-26", end="2022-2-26")
SOL = yf.download(Solana, start="2022-2-26", end="2022-2-26")

# btc
st.write("BITCOIN ($)")
imageBTC = Image.open(
    urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
st.image(imageBTC)
st.table(BTC)
st.bar_chart(BTC_His.Close)


# eth
st.write("ETHEREUM ($)")
imageETH = Image.open(
    urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
st.image(imageETH)
st.table(BTC)
st.bar_chart(ETH_His.Close)


# xrp
st.write("RIPPLE ($)")
imageXRP = Image.open(
    urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"))
st.image(imageXRP)
st.table(BTC)
st.bar_chart(XRP_His.Close)


# bch
st.write("BITCOIN CASH ($)")
imageBCH = Image.open(
    urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"))
st.image(imageBCH)
st.table(BTC)
st.bar_chart(BCH_His.Close)


# usdt
st.write("TETHER ($)")
imageUSDT = Image.open(
    urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/825.png"))
st.image(imageUSDT)
st.table(BTC)
st.bar_chart(USDT_His.Close)


# sol
st.write("SOLANA ($)")
imageSOL = Image.open(
    urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png"))
st.image(imageSOL)
st.table(BTC)
st.bar_chart(SOL_His.Close)
