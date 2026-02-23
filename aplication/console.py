# consoleを対応

from tools.tools_logger import Logger
from lib.tk_lib import TkLib

class Console:
    
    def __init__(self):
        
        self.__log = Logger("Console")
        self.__tk = TkLib("console画面", "300x150")
        
    def console_run(self):
        """ console画面を出力 """

        self.__tk.tkinter_label_size("hellow", 0.5, 0.5, "n", 60)
        self.__tk.root_loop()