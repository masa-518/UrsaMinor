# 自動音声を行うクラス

import pyttsx3

from tools.tools_logger import Logger

class AutoVoice:
    
    def __init__(self):
        
        self.__log = Logger("AutoVoice")
        
    def voice_txt(self, mes):
        
        engine = pyttsx3.init()
        self.__log.print_info("voice txt initialize finish")
        self.__log.print_info(f"voice txt -> {mes}")
        engine.say(mes)
        engine.runAndWait()