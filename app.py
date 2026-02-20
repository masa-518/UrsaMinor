# アプリケーション

from tools.tools_logger import Logger
from lib.autovoice import AutoVoice
from aplication.console import Console

class App:
    
    def __init__(self):
        
        self.__auto_voice = AutoVoice()
        
        
    def run(self):
        """ 実行部分 """
        
        self.__auto_voice.voice_txt("こんにちは")
        console = Console()
        console.console_run()

    