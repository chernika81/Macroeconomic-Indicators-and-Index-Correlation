

from flask import Flask, request, render_template
import pickle
import pandas as pd
import yfinance as yf
import streamlit as st






#Create an app object using the Flask class. 
# app = Flask("stock predictor")
app=Flask(__name__,template_folder='templates')


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
        model = pickle.load(open('DJRFmodel.pkl', 'rb'))

        Start = request.form['Start Date']
        End = request.form['End Date']

        ticker = request.form['ticker'].upper()
    stock = yf.Ticker(ticker)
    stocks_df = stock.history(start=Start, end=End)


    print(stocks_df.head())

    test_data = stocks_df[['Open', 'High', 'Low','Volume' ]].tail(5)

    predicted_stock_price = model.predict(test_data)
    return render_template('result.html',   predicted_price=predicted_stock_price)
    

if __name__ == "__main__":
    app.run(debug=True)