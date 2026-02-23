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
    
    def tkinter_label(self, text, relx, rely, anchor):
        """ ラベル表示 """
        label = tk.Label(self.__root, text=text, font=("Helvetica"))
        label.place(relx=relx, rely=rely, anchor=anchor)

    def tkinter_label_size(self, text, relx, rely, anchor, size):
        """ ラベル表示 文字の大きさ指定 """
        label = tk.Label(self.__root, text=text, font=("Helvetica", size))
        label.place(relx=relx, rely=rely, anchor=anchor)
    
    def tkinter_entry(self, width, relx, rely, anchor):
        """ Entry表示 """
        
        entry = tk.Entry(self.__root, width=width)
        entry.place(relx=relx, rely=rely, anchor=anchor)
        return entry
    
    def 

    def root_loop(self):
        self.__root.mainloop()


