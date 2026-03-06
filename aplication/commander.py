# コマンド管理クラス

from tools.tools_logger import Logger
from lib.finance import Finance
from window.window_usjp_rate import UsdFxWindow

class Commander:

    def __init__(self):

        self.__log = Logger("Commander")

        
    def select_command_for_console(self, com):
        """ console入力されたコマンドから、呼び出す関数を選択する """

        self.__log.print_info(f"entry command:{com}")

        if com == "hellow":
            self.__hellow()
        
        elif com == "finance test":
            self.__finance_direct_lib_finance()
            
        elif com == "finance usdjpy":
            self.__finance_usd_jpy_rate()
        
        else:
            self.__log.print_warn("Unknown Comand")


    def __hellow(self):
        """ commander疎通確認コマンド
        hellow を表示させる
        """
        self.__log.print_info("Command: hellow")

    def __finance_direct_lib_finance(self):
        """ finance 単体動作確認コマンド
        finance のlibへ直接アクセスをすることができる
        """
        self.__log.print_info("Command: finance test")

        yet = Finance("USDJPY=X")
        date = yet.get_rate_download_period_interval("1d", "1h")
        print(date["Close"])
        
    def __finance_usd_jpy_rate(self):
        
        self.__log.print_info("Command: finance usdjpy")
        
        yet = UsdFxWindow()
