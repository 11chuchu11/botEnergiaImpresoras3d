from pyfirmata2 import Arduino, util

class ArduinoController:
    def __init__(self, port, pins={}):
        self.board = Arduino(port)
        self.it= util.Iterator(self.board)
        self.it.start()
        
    def declare_pin(self,name):
        print()
