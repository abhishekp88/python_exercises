import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = '06QH43QF6RPXTHT1'
NEWS_API_KEY = 'fcc7566647194774b3b747bd04cfb1a6'

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
get_stock_info = requests.get(STOCK_ENDPOINT, stock_params)
# print(get_stock_info.json()['Time Series (Daily)'])
data = get_stock_info.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]

yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

dfference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(dfference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percentage = (dfference / float(yesterday_closing_price)) * 100
print(diff_percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if diff_percentage > 5:
    NEWS_API_PARAM = {
        "apikey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, NEWS_API_PARAM)
    news_response_json = news_response.json()['articles']
    # print(news_response_json)



#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
top_3_news = news_response_json[:3]
# print(top_3_news)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_list = [f"Headline : {article['title']}. \nBrief: {article['description']}" for article in top_3_news]
print(formatted_list)

#TODO 9. - Send each article as a separate message via Twilio. 



