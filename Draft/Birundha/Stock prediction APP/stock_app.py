import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
import yfinance as yf
import streamlit as st




#Create an app object using the Flask class. 
app = Flask("stock predictor")


@app.route('/')
def home():
    return(
    # f"Choose one stock index name as :<br/>",
    render_template('index input.html')
    )


@app.route('/predict',methods=['POST'])
def predict():
    form = request.form
    if request.method == 'POST':
      #Load the trained model. (Pickle file)
        model = pickle.load(open('model/DJRFmodel.pkl', 'rb'))

        year = request.form['year']
        ticker = request.form['ticker'].upper()
    print("hello world")
    period = year *365
    
    stock = yf.Ticker(ticker)
    stocks_df = stock.history()
    # stocks_df = yf.download("ticker", start='2008-09-01', end=None)##error  Exception('%ticker%: No timezone found, symbol may be delisted')  


    print(stocks_df.head())

    test_data = stocks_df[['Open', 'High', 'Low' ]].tail(1)

    predicted_stock_price = model.predict(test_data)
    return render_template('result.html',   predicted_price=predicted_stock_price)
    

if __name__ == "__main__":
    app.run(debug=True)