import requests as rq


AV_FUNCTION = "TIME_SERIES_DAILY"
AV_COMPANY = "TSLA"
AV_API_KEY = "0FOAMLJQDISX0D59"
AV_URL = f"https://www.alphavantage.co/query"

av_params = {
    "function": AV_FUNCTION,
    "symbol": AV_COMPANY,
    "apikey": AV_API_KEY,
}

stocks_data = rq.get(AV_URL, params=av_params).json()["Time Series (Daily)"]
closes = [float(value["4. close"]) for (key, value) in stocks_data.items()]
# one_day_ago_str = str(datetime.date.today() - datetime.timedelta(days=1))
# two_days_ago_str = str(datetime.date.today() - datetime.timedelta(days=2))
#one_day_ago_stock_price = stocks_data[one_day_ago_str]["4. close"]
one_day_ago_stock_price = closes[0]
two_days_ago_stock_price = closes[1]
#two_days_ago_stock_price = stocks_data[two_days_ago_str]["4. close"]
stock_diff = round(two_days_ago_stock_price - one_day_ago_stock_price, 4)
stock_percentage = int((stock_diff/one_day_ago_stock_price)*100)
print(f"Stock change is {stock_diff} with percentage of {stock_percentage}%")
