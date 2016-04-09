class document():
    def __init__(self):
        pass
    def read(self):
        with document.open("r"):
            read=document.read()
        document.close()
        return read
