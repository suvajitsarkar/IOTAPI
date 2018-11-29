from Right import *
from Arduino import *
class RightC:
    def __init__(myobj):
        myobj.color = Color(2)
        myobj.temp = Temperature()
    def seeColor(self):
        print "Color ", self.color.getColor()
    def seeTemperature(self):
        print "Temperature ", self.temp.getTemperature()

abc = RightC()
abc.seeColor()
abc.seeTemperature()
abc.seeColor()
d=Dht()
print("Cool")
d.updateValue()
if d.getValueHumidity()>60:
    print "Humidity High"
    abc.color.postData()
else:
    print "Humidity Low"

