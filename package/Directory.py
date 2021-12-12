import os
import shutil

class Directory:

    # ディレクトリ作成
    def folder_make(self,PATH_MAKE):

        if os.path.exists(PATH_MAKE) == False:
            os.mkdir(PATH_MAKE)

    #ファイル　コピー   
    def copy_file(self,PATH_FILE_ORIGINAL,PATH_FILE_COPY):
            
        if os.path.exists(PATH_FILE_COPY) == False:        
            shutil.copyfile(PATH_FILE_ORIGINAL, PATH_FILE_COPY)