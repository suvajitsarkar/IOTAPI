from .Gather import gatherclass
from .DatabaseC import dbEntry
import time
class Mq2:
    def __init__(self,idn,value=0):
        self.idn=idn
        self.smoke=value
        self.g=gatherclass()
    def getValue(self):
        return self.smoke
    def updateValue(self):
        self.g.gather(self,"Smoke")
    def insertDB(self):
        sql="insert into MQ2(id, smoke) values('%s','%d')"%(self.idn,float(self.smoke))
        dbEntry(sql)
if __name__ == "__main__":
    d=Mq2("MQ2_1")
    d.updateValue()
    print(d.getValue(),time.ctime())
    d.insertDB()
