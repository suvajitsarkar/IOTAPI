from Gather import gatherclass
from DatabaseC import dbEntry
import time
from thinkSpeak import updateCloud
class Mq135:
    def __init__(self,idn,value=0):
        self.idn=idn
        self.amonia=value
        self.g=gatherclass()
    def getValue(self):
        return self.amonia
    def updateValue(self):
        self.g.gather(self,"Amonia")
    def insertDB(self):
        if self.amonia != None:
            sql="insert into MQ135(id, amonia) values('%s','%d')"%(self.idn,float(self.amonia))
            dbEntry(sql)
if __name__ == "__main__":
    while True:
        d=Mq135("MQ135_1")
        d.updateValue()
        print(d.getValue(),time.ctime())
        d.insertDB()
        updateCloud("6VIW5JTUAZ6UILO8", d.getValue())
