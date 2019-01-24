import time
import serial
class gatherclass:
    def __init__(self):
        self.ser=serial.Serial("/dev/ttyUSB1",115200)
        self.ser.baudrate=115200
        #print(self.ser.readline().decode("utf-8"))
    def gatherString(self):
        #bytesToRead = self.ser.inWaiting()
        #return self.ser.read(bytesToRead)        
        return self.ser.readline().decode("utf-8")
    def parseString(self,string,type):
        temp=string.split(",")
        for i in temp:
            j=i.split(":")
            if j[0]=="Temperature" and type=="T":
                return j[1]
            if j[0]=="Humidity" and type=="H":
                return j[1]
            if j[0]=="Ammonia" and type=="A":
                return j[1]
            if j[0]=="Smoke" and type=="S":
                return j[1]
    def gather(self,obj,type):
        try:
            string=self.gatherString()
            print(time.ctime(),string)
            t=self.parseString(string,"T")
            h=self.parseString(string,"H")
            a=self.parseString(string,"A")
            s=self.parseString(string,"S")
            if type == "TH":
                obj.temperature=t
                obj.humidity=h
            elif type == "Amonia":
                obj.amonia=a
            elif type == "Smoke":
                obj.smoke=s
            else:
                print("Wrong Parameter...")
        except Exception as e:
            print("Don't ",e)
