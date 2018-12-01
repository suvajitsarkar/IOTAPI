import Gather
from DatabaseC import dbEntry
class Dht:
	def __init__(self,idn,t=0,h=0):
		self.idn=idn
                self.temperature=t
		self.humidity=h
	def getValueTemperature(self):
		return self.temperature
	def getValueHumidity(self):
		return self.humidity
        def updateValue(self):
            Gather.gather(self,"TH")
        def insertDB(self):
            sql="insert into DHT(id, temperature, humidity) values('%s','%d','%d')"%(self.idn,float(self.temperature),float(self.humidity))
            dbEntry(sql)
d=Dht("DHT1")
d.updateValue()
print d.getValueTemperature()
print d.getValueHumidity()
#d.insertDB()
