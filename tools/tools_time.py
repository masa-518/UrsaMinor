# 時間関連のクラス

import time
from datetime import datetime

class ToolsTime:
    """ 時間関連のクラス """
    
    def __inti__(self):
        pass
    
    def __get_time(self):
        
        return datetime.now()
    
    def set_time_for_log(self):
        
        return self.__get_time().strftime("%Y-%m-%d_%H:%M:%S")
    
    def set_time_for_log_txt(self):
        return self.__get_time().strftime("%Y%m%d_%H%M%S")

