#GUI 出力

import tkinter as tk
from tools.tools_logger  import Logger

class TkLib:
    
    def __init__(self, title, size):
        
        self.__log = Logger("TkLib")
        self.__title = title
        self.__size = size
        self.__root = None
        
        self.__tkinter_initialize()
        
    def __tkinter_initialize(self):
        """ 画面出力の初期化 """
        self.__root =  tk.Tk()
        self.__root.title(self.__title)
        self.__root.geometry(self.__size)
        self.__log.print_info(f"tkinter initialise title:{self.__title}, size:{self.__size}")
    
    def root_loop(self):
        self.__root.mainloop()


