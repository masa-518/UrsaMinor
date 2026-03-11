#USDJPYの為替を取得するためのwindow

from tools.tools_logger import Logger
from lib.tk_lib import TkLib
from aplication.fx_usdjpy import FxUsdJpy

class UsdFxWindow:
    
    def __init__(self):
        
        self.__log = Logger("UsdFxWindow")
        self.__tk = TkLib("UsdJpy画面", "700x800")
        self.__finance = FxUsdJpy()
        self.__rate_comander()
        self.__run_window()
        
    def __rate_comander(self):
        """ command名を宣言する """
        
        self.GET_INFORMATION_RATE = "get information rate"
        
        # コマンドをリスト化
        self.__comand_list = [self.GET_INFORMATION_RATE]
    
    def __run_window(self):

        self.__log.print_info("usd-jpy windw start")
        self.__tk.tkinter_label("Fx UsdJpy", 0.1, 0.05, "center")
        self.__comand = self.__tk.tkinter_combobox(30, self.__comand_list, 0.1, 0.10, "w")
        print(type(self.__comand))
        self.__tk.tkinter_label("period", 0.1, 0.15, "w")
        self.__period =  self.__tk.tkinter_entry(15, 0.2, 0.15, "w")
        self.__tk.tkinter_label("interval", 0.1, 0.20, "w")
        self.__interval =  self.__tk.tkinter_entry(15, 0.2, 0.20, "w")
        self.__tk.tkinter_button("run", self.__button_run , 0.8, 0.1, "center")

    def __button_run(self):
        
        com = self.__comand.get()
        self.__log.print_info(f"command:{com}")
        
        # コマンドの種類で実行を切り替える
        if com == self.GET_INFORMATION_RATE:
            

            self.__finance.get_rate_usdjpy(self.__period.get(), self.__interval.get())