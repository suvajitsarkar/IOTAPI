from Right import *
class RightC:
    def __init__(myobj):
        myobj.color = Color()
        myobj.temp = Temperature()
    def seeColor(self):
        print "Color ", self.color.getColor()
    def seeTemperature(self):
        print "Temperature ", self.temp.getTemperature()

abc = RightC()
abc.seeColor()
abc.seeTemperature()
abc.color.postData()
abc.seeColor()
