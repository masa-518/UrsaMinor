# txtファイルを作成する
import os
import shutil

from tools.tools_time import ToolsTime

class ContTxt:
    
    def __init__(self):
        
        self.__time = ToolsTime()
        
        self.__name_temp_txt = "temp.txt"
        self.__name_log_folder = "log"
        self.__path_log_folder = os.path.join(os.getcwd(), self.__name_log_folder)
        self.__path_temp_txt = os.path.join(self.__path_log_folder, self.__name_temp_txt)
    
    def make_temp_log_txt(self):
        """ txt tempを一新する """
        
        if os.path.exists(self.__path_temp_txt):
            os.remove(self.__path_temp_txt)
            
        with open(self.__path_temp_txt, "w", encoding="utf-8") as f:
            pass
        
    def write_temp_log(self, mes):
        """ ログtempにメッセージを書く """
        self.write_txt(self.__path_temp_txt, mes)
            
    def write_txt(self, path, mes):
        """ txtにメッセージを書く """
        with open(path, "a", encoding="utf-8") as f:
            f.write(mes + "\n")
            
    def copy_temp_log(self):
        """ tempフォルダーのログをコピー """
        
        file_name = self.__time.set_time_for_log_txt() + ".txt"
        path = os.path.join(os.getcwd(), self.__name_log_folder, file_name)
        self.copy_txt(self.__path_temp_txt, path)
        
    def copy_txt(self, from_path, to_path):
        """ txtファイルをコピー """
        shutil.copy2(from_path, to_path)