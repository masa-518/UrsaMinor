# Main関数

from tools.tools_logger import Logger

class Main:
    
    def __init__(self):
        self.__log = Logger("Main")

    def run(self):
        """ 実行部分 """

        self.__initialize()
        self.__app()
        self.__end_process()

    def __app(self):
        """ appクラス転送する """
        self.__log.print_info("Main App")
    
    def __initialize(self):
        """ 最初に実施する内容 """
        
        self.__log.make_temp_log_txt()
        # 下記以降に記載しないとログが残らない
        
    def __end_process(self):
        """ 最後に実施する内容 """
        
        
        self.__log.copy_log()
        # ここでログが切れるのでこれ以降は追加しない
        
if __name__ == "__main__":
    
    print("Hellow")
    print("===================================================================")
    main = Main()
    main.run()