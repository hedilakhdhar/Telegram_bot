from .credentials import av_token
from alpha_vantage.timeseries import TimeSeries
import pandas as pd



def get_financial_data(symbol):
    #url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED'
    #&symbol=MSFT&apikey=demo'
    #params = {'symbol':index}
    #headers = {'apikey':av_token}

    #r = requests.get(url, headers=headers, params=params).json()

    ts = TimeSeries(key='azkd', output_format='pandas')

    data, meta_data = ts.get_weekly_adjusted(symbol=symbol)

    begin = pd.Timestamp('2019-01-04 00:00:00')
    last = data.index.max()

    perf =  (data.loc[last , '5. adjusted close'] - data.loc[begin , '5. adjusted close']
        )/ data.loc[begin , '5. adjusted close']

    return perf
