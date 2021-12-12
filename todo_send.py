from linebot import LineBotApi
from linebot.models import TextSendMessage
import traceback
from package.Const import Const
from package.Const_secret import Const_secret
from package.Directory import Directory
from package.TxtFile import TxtFile

if __name__ == '__main__':
    
    const_token = Const_secret()
    CHANNEL_ACCESS_TOKEN = const_token.CHANNEL_ACCESS_TOKEN
    USER_ID = const_token.USER_ID
        
    try:
        
        #　定数
        const = Const()
        PATH_TODO_TOMMOROW_YEAR = const.PATH_TODO_TOMMOROW_YEAR
        PATH_TODO_TOMMOROW_MONTH = const.PATH_TODO_TOMMOROW_MONTH
        PATH_TODO_TOMMOROW_DAY = const.PATH_TODO_TOMMOROW_DAY
        PATH_TODO_TODAY_DAY = const.PATH_TODO_TODAY_DAY

        # 明日のtodoディレクトリ作成
        directory = Directory()
        directory.folder_make(PATH_TODO_TOMMOROW_YEAR)
        directory.folder_make(PATH_TODO_TOMMOROW_MONTH)

        # 今日のやつを明日のやつにコピー
        directory.copy_file(PATH_TODO_TODAY_DAY,PATH_TODO_TOMMOROW_DAY)

        # 今日のTODOを送信
        txtFile = TxtFile()
        TODO_TODAY = txtFile.read_file(PATH_TODO_TODAY_DAY)
        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
        line_bot_api.push_message(USER_ID, TextSendMessage(text=TODO_TODAY))

    except Exception as e:

        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
        line_bot_api.push_message(USER_ID, TextSendMessage(text='エラー発生\n' + traceback.format_exc()))
