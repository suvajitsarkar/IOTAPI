import serial
from xbee import ZigBee
from DatabaseC import dbEntry
class xbee1:
    def __init__(self,idn,temp=1023,twister=0):
        self.idn=idn
        self.temperature=temp
        self.twister=twister
    def updateValue(self):
        try:
            ser = serial.Serial('/dev/ttyUSB1')
            s1=1023
            #by=ser.read().hex()
            xbe= ZigBee(ser)
            #return by
            d=xbe.wait_read_frame()
            l=d.get('samples')
            adc0=l[0].get('adc-0')
            adc1=l[0].get('adc-1')
            dio2=l[0].get('dio-2')
            #print(adc0,adc1,dio2)
            if(adc0>0):
                s1=(3.3*adc0)/1023
                s1=(s1*1000-500)/100
            #print(int(str(a),16),int(str(b),16),c)
            #print("Temperature ",s1)
            self.temperature=s1
            self.twister=adc1
        except Exception as e:
            print(e," Hello")
    def getTemperature(self):
        return self.temperature
    def getTwister(self):
        return self.twister
    def insertDB(self):
        sql="insert into Xbee(id, temperature, twister) values('%s','%f','%d')"%(self.idn,float(self.temperature),float(self.twister))
        dbEntry(sql)
'''x= xbee1("Xbee_1")
while(1):
    x.readdata()
    print("Temperature= ",x.getTemperature())
    print("Twister= ",x.getTwister())
    x.insertDB()'''
