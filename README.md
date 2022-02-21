# Sentiment-based Portfolio Selection Using Machine Learning : Project Highlight 
* Explored the predictive values of daily pollical news and financial news on prediction models, which have not been studied in prior work.
* Scraped over 200,000 news articles from Bloomberg, The Guardian, Reuter, investing.com, etc. Foreign news articles were translated to English using Yandex API.
* Created a prediction model that forecasts stock trends next month to help investors chose what profitable stocks to include in their portfolio.
* Test models on two types of countries, including developed and developing countries (Australia, US, Vietnam) to confirm the stability of models. 
## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, scrapy, vaderSentiment, nltk, LoughranMcDonalds, hyperopt, PyPortfolioOpt, investpy
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  


## Project Summary 
![poster](https://user-images.githubusercontent.com/81540274/154918807-9000a639-6437-4816-adb1-aca54d11ce72.png)
## Datasets 
![Dataset](https://user-images.githubusercontent.com/81540274/154919145-226d8822-d678-4246-b368-d75590c0ddfc.png)
## Methodology
Overview, the research includes 2 stages (i) using machine learning to predict stock trends in the next 21 days. (ii) chose stocks with the highest probability of uptrend to form a trading portfolio, and using mean-variance method to allocate the weight of each stock so that the portfolio are maximised in profits. 
![framework](https://user-images.githubusercontent.com/81540274/154919645-a990f5b4-1c6a-4299-90b1-884a1922d072.png)
## Data Processing - Sentiment Analysis
 
Sentiment analysis is used to retrieve sentiment for each stock by calculating sentiment value of all financial articles related to each stock in a day. 
Sentiment value from political news is the average sentiments of all political articles collected daily. 
![SA](https://user-images.githubusercontent.com/81540274/154921186-4da1ba25-2599-4e7b-8fe1-3e95c87ef492.png)
## Data Processing - Technical Analysis
![TA](https://user-images.githubusercontent.com/81540274/154921568-61aec09a-f308-4abd-9147-4b934b4dd4c6.png)
## Model Inputs
![inputs](https://user-images.githubusercontent.com/81540274/154925497-bf2893b8-8c93-42d6-a8ec-d3fd14b3d385.png)
## Model Building 
   
I tried different models and evaluated them using F1. I chose F1 based on the practical purpose of the research - predict and chose stocks with the highest probability of up-trend. Therefore, the more up-trend stocks we have in our portfolio, the more profittable our portfolios will be guaranteed. 
XGB outperformed the others by performance and execution time (the shortest running time). Therefore, XGB is a good fit to run in large scale. 
![algorithms](https://user-images.githubusercontent.com/81540274/154922128-e4e29d68-151c-4251-b48c-b41251f6dfda.png)
## Data Split
As financial time series is non-stationary and complex, this approach is considered is prevent look-ahead bias and data leakage associated with the random sampling of the training and test data sample.
![datasplit](https://user-images.githubusercontent.com/81540274/154924662-81ae8dbb-60e6-4155-8665-110f9bcb2093.png)
## Project Outcomes
![finding1](https://user-images.githubusercontent.com/81540274/154925219-aa2e138f-9cad-4f04-8d53-883ea476bd97.png)
![finding2](https://user-images.githubusercontent.com/81540274/154926396-c91721c6-24a3-435b-ac7a-d661bd628656.png)
