#ドル円相場の取得

from lib.finance import Finance
from tools.tools_logger import Logger

class FxUsdJpy:
    
    def __init__(self):
        
        self.__ticker = "USDJPY=X"
        self.__log = Logger("FxUsdJpy")
        self.__finance_lib = Finance(self.__ticker)
        self.__rate = None
    
    def get_rate_usdjpy(self, period, interval):
        
        return self.__finance_lib.get_rate_download_period_interval(period, interval)
