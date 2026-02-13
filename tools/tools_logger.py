# ログの出力

from tools.tools_time import ToolsTime
from tools.tools_cont_txt import ContTxt

class Logger:
    
    def __init__(self, module):
        
        self.__module = module
        self.__time = ToolsTime()
        self.__cont_txt = ContTxt()
        
        # debugログの出力をするならばTrueにする。
        self.__is_print_debug = True
    
    def print_info(self, mes):
        
        mes = self.__time.set_time_for_log() + f" [INFO]<{self.__module}> " + mes
        print(mes)
        self.__write_temp_log(mes)

    def print_error(self, mes):
        
        mes = self.__time.set_time_for_log() + f" [ERROR]<{self.__module}> " + mes
        print(mes)
        self.__write_temp_log(mes)


    def print_warn(self, mes):
        
        mes = self.__time.set_time_for_log() + f" [WARN]<{self.__module}> " + mes
        print(mes)
        self.__write_temp_log(mes)


    def print_debug(self, mes):
        
        if self.__is_print_debug is False:
            return

        mes = self.__time.set_time_for_log() + f" [DEBUG]<{self.__module}> " + mes
        print(mes)
        self.__write_temp_log(mes)

        
    def make_temp_log_txt(self):
        self.__cont_txt.make_temp_log_txt()
        
    def __write_temp_log(self, mes):
        self.__cont_txt.write_temp_log(mes)
        
    def copy_log(self):
        self.__cont_txt.copy_temp_log()