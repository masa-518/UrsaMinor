#USDJPYの為替を取得するためのwindow

from tools.tools_logger import Logger
from lib.tk_lib import TkLib

class UsdFxWindow:
    
    def __init__(self):
        
        self.__log = Logger("UsdFxWindow")
        self.__tk = TkLib("UsdJpy画面", "700x800")
        
    def __run_window(self):
        
        