import time
import serial
def gatherString():
    ser=serial.Serial("/dev/ttyUSB1",115200)
    ser.baudrate=115200
    return ser.readline().decode("utf-8")

def parseString(string,type):
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

def gather(obj,type):
    try:
        string=gatherString()
        print(time.ctime(),string)
        t=parseString(string,"T")
        h=parseString(string,"H")
        a=parseString(string,"A")
        s=parseString(string,"S")
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
    

