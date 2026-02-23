# consoleを対応

from tools.tools_logger import Logger
from lib.tk_lib import TkLib
from lib.autovoice import AutoVoice

class Console:
    
    def __init__(self):
        
        self.__log = Logger("Console")
        self.__tk = TkLib("console画面", "300x150")
        self.__auto_voice = AutoVoice()
        self.__console_entry = None
        
    def console_run(self):
        """ console画面を出力 """

        self.__log.print_info("console windw start")
        self.__auto_voice.voice_txt("console 画面")
        self.__tk.tkinter_label("console", 0.12, 0.2, "center")
        self.__console_entry = self.__tk.tkinter_entry(40, 0.03, 0.33, "w")
        self.__tk.tkinter_button("run", self.button_run , 0.5, 0.55, "center")

        self.__tk.root_loop()

    def button_run(self):
        self.__log.print_info("conmand run")
        self.__log.print_debug(f'entry txt: {self.__console_entry.get()}')

        