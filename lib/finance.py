#finance関連のクラス

import yfinance as yf
from tools.tools_logger import Logger

class Finance:

    def __init__(self, ticker):
        self.__log = Logger("Finance")
        self.__ticker = ticker

    def get_rate_object(self):
        """ tickerオブジェクトを取得する """
        yet =  yf.Ticker(self.__ticker)
        self.__log.print_info("Success download rate history")
        return yet
    
    def get_rate_period(self, period):
        """ 期間を指定オブジェクトを指定する """
        yet = self.get_rate_object().history(period=period)
        self.__log.print_info("Success download rate history period")
        return yet
    
    def get_rate_download_period_interval(self, period, interval):
        """ 期間と範囲を指定して為替データを取得する """
        yet =  yf.download(tickers= self.__ticker, period = period, interval = interval)
        
        self.__log.print_info("Success download rate")
        
        return yet
