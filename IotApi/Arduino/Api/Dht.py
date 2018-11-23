import Gather
class Dht:
	def __init__(self,t=0,h=0):
		self.temperature=t
		self.humidity=h
	def getValueTemperature(self):
		return self.temperature
	def getValueHumidity(self):
		return self.humidity
        def updateValue(self):
            Gather.gather(self,"TH")
d=Dht()
print "Hello"
d.updateValue()
print "Done"
print d.getValueTemperature()
print d.getValueHumidity()
