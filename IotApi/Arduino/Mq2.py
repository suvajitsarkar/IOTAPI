import Gather
from DatabaseC import dbEntry
class Mq2:
	def __init__(self,idn,value=0):
            self.idn=idn
            self.smoke=value
	def getValue(self):
            return self.smoke
        def updateValue(self):
            Gather.gather(self,"Smoke")
        def insertDB(self):
            sql="insert into MQ2(id, smoke) values('%s','%d')"%(self.idn,float(self.smoke))
            dbEntry(sql)
'''d=Mq2("MQ2_1")
d.updateValue()
print d.getValue()
d.insertDB()'''
