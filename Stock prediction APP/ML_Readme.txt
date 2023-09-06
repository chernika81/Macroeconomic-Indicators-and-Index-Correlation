Project 4:Stock Indexes vs Macroeconomic Indicators 

Synopsis

This project is to determine how the stock indexes(we have used 3 different stock indexes such as The Dow Jone, Nasdaq and the S&P)
stand up against various macroeconomic factors (CStock Indexes vs Macroeconomic Indicators PI, Unemployment, FedRate (interest rates) and Inflation).
We used these factors to then build a Machine Learning Model to determine how the Indexes will perform in the future.


Data Sources
We have found multiple excel sheets via Kaggle to be used and cleaned for our project. 
1.Daily open, close high and low for Dow Jones, Nasdaq and S&P from 1/2/2008 to present  (we then took the averages of the open and close) 
2.Daily Inflation  & Fed Funds 
3.Monthly CPI and Unemployment rate 
4.Yfinance package

Tools Used
1.Python Pandas
2.Python Matplotlib
3.Machine Learning 
4.Tableau

Processing Data
1.The data has been etracted from different data sources ,transformed to the appropriate format (date) and cleaned by droping Nan

Initial Analysis
Source code:addingothermacro.ipynb

Once the data was cleaned, the linear correlation between the stock average and CPI ,inflation rate and unemployment rate has been evaluated
to see what the highest correlation was.
The highest correlation was between the indexes and CPI (S&P  VS CPI at 0.95) 
The lowest correlation was Inflation rate and the indexes (S&P was at 0.23) 


Machine learning Model

1. A machine learning model(DJRFmodel) has been created using Random forest Regressor to predict closing stock price
for Dow jones using Dow jones stock history.
And the model is deployed to use in Flask APP

The r-squared score is 98% 
--Source code: stockprediction-ML.ipynb

2.Another regressor model will predict the impact of DJ’s stock price based on Macro 
economic indicators (CPI,FDD, Inflation Rate, unemployment rate)
----Source code: stockprediction-ML.ipynb


3. A basic flask APP is created to predict DJ stock price using the model --DJRFmodel , which will ask for the stock 
ticker name(^DJI) and the start ,End date .The  app will run in local host 
http://127.0.0.1:5000/.

--stock_app.py

Conclusion:
Expected that key U.S. macroeconomic indicators like unemployment, inflation and 
CPI and FDD were going to be among the highly ranked features.
While the stock market is influenced by a many factors, the CPI can significantly 
influence swings in performance. For instance, reactionary Fed moves can directly 
impact corporate profits and economic growth, leading the stock value to fluctuate 
drastically. Higher Fed rate hikes based on CPI often cause the market to dip or slow 
as traders want to hedge their bets.



