# コマンド管理クラス

from tools.tools_logger import Logger

class Commander:

    def __init__(self):

        self.__log = Logger("Commander")

        
    def select_command_for_console(self, com):
        """ console入力されたコマンドから、呼び出す関数を選択する """

        self.__log.print_info(f"entry command:{com}")

        if com == "hellow":
            self.__hellow()
        
        else:
            self.__log.print_warn("Unknown Comand")


    def __hellow(self):
        self.__log.print_info("Command: hellow")