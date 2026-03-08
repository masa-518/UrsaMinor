#USDJPYの為替を取得するためのwindow

from tools.tools_logger import Logger
from lib.tk_lib import TkLib

class UsdFxWindow:
    
    def __init__(self):
        
        self.__log = Logger("UsdFxWindow")
        self.__tk = TkLib("UsdJpy画面", "700x800")
        self.__run_window()
        
    def __run_window(self):

        self.__log.print_info("usd-jpy windw start")
        self.__tk.tkinter_label("Fx UsdJpy", 0.1, 0.05, "center")
        