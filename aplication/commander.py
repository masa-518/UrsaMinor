# コマンド管理クラス

from tools.tools_logger import Logger

class Commander:

    def __init__(self):

        self.__log = Logger("Commander")

        #下記に実行コマンドを表示させる
        
        self.COMMAND_HELLOW = "hellow"