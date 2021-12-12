

class TxtFile:

    def read_file(self,PATH_FILE):
        fd = open(PATH_FILE, mode='r')
        data = fd.read()
        fd.close()

        return data

