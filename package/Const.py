import datetime
from package.Const_secret import Const_secret
const_secret = Const_secret()

class Const:

    def __init__(self):

        #　テキストファイルのパス
        PATH_TODO = const_secret.PATH_TODO
        PATH_TODO_TODAY_YEAR = PATH_TODO + '/' +  datetime.datetime.now().strftime('%Y')
        PATH_TODO_TODAY_MONTH = PATH_TODO_TODAY_YEAR + '/' +  datetime.datetime.now().strftime('%Y%m')
        self.PATH_TODO_TODAY_DAY = PATH_TODO_TODAY_MONTH + '/' +  datetime.datetime.now().strftime('%Y%m%d') + '.md'
        self.PATH_TODO_TOMMOROW_YEAR = PATH_TODO + '/' +  (datetime.datetime.now() + + datetime.timedelta(days = 1)).strftime('%Y')                
        self.PATH_TODO_TOMMOROW_MONTH = self.PATH_TODO_TOMMOROW_YEAR + '/' +  (datetime.datetime.now() + + datetime.timedelta(days = 1)).strftime('%Y%m')
        self.PATH_TODO_TOMMOROW_DAY = self.PATH_TODO_TOMMOROW_MONTH + '/' +  (datetime.datetime.now() + + datetime.timedelta(days = 1)).strftime('%Y%m%d') + '.md'
