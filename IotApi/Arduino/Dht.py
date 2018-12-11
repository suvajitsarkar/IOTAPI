from .Gather import gatherclass
from .DatabaseC import dbEntry
import time
class Dht:
    def __init__(self,idn,t=0,h=0):
        self.idn=idn
        self.temperature=t
        self.humidity=h
        self.g=gatherclass()
    def getValueTemperature(self):
        return self.temperature
    def getValueHumidity(self):
        return self.humidity
    def updateValue(self):
        self.g.gather(self,"TH")
    def insertDB(self):
        sql="insert into DHT(id, temperature, humidity) values('%s','%d','%d')"%(self.idn,float(self.temperature),float(self.humidity))
        dbEntry(sql)
if __name__ =="__main__":
    d=Dht("DHT_1")
    d.updateValue()
    print(d.getValueTemperature(),d.getValueHumidity(),time.ctime())
    d.insertDB()
