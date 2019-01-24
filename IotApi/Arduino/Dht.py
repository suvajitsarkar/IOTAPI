from Gather import gatherclass
from DatabaseC import dbEntry
from thinkSpeak import updateCloud
import time
import http.client, urllib
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
'''
    def updateCloud(self,key,f1,f2):
        params = urllib.parse.urlencode({'field1': self.temperature, 'field2': self.humidity, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            print("OK Till here")
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
'''
if __name__ =="__main__":
    d=Dht("DHT_1")
    while True:
        d.updateValue()
        print(d.getValueTemperature(), d.getValueHumidity(), time.ctime())
        #d.insertDB()
        updateCloud("6RLEWPCH6P7N10U5", d.getValueTemperature(), d.getValueHumidity())
