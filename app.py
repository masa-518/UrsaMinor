# アプリケーション

from tools.tools_logger import Logger
from lib.autovoice import AutoVoice

class App:
    
    def __init__(self):
        
        self.__auto_voice = AutoVoice()
        
    def run(self):
        """ 実行部分 """
        
        self.__auto_voice.voice_txt("こんにちは")

        