import requests
from DatabaseC import dbEntry
import time
from thinkSpeak import updateCloud
url1 = 'http://192.168.0.4:8080/rest/items/Color1/'
url2 = 'http://192.168.0.4:8080/rest/items/HueColorLamp3_Color/'
url3 = 'http://192.168.0.4:8080/rest/items/HueColorLamp3_ColorTemperature/state'
url4 = 'http://192.168.0.4:8080/rest/items/HueColorLamp1_ColorTemperature/state'
api1 = '6PXRQW3QSAH7EELA'
api2 = 'KW9UKEZGSVXYJD25'
class Color:
    def __init__(myobj,idn):
        myobj.idn=idn
        myobj.updateValue()
    def getColor(myobj):
        return myobj.color
    def getSaturation(myobj):
        return myobj.saturation
    def getBrightness(myobj):
        return myobj.brightness
    def getTemperature(myobj):
        return myobj.temperature
    def updateValue(myobj):
        data = ''
        if myobj.idn=="Hue_1":
            response = requests.get(url1+'state', data=data)
            response_t = requests.get(url3, data=data)
        else:
            response = requests.get(url2+'state', data=data)
            response_t = requests.get(url4,data=data)
        x = response.text.split(",")
        print(time.ctime(),x[0],x[1],x[2],response_t.text)
        myobj.color=x[0]
        myobj.saturation= x[1]
        myobj.brightness = x[2]
        myobj.temperature = response_t.text
    def postData(myobj,data):
        if myobj.idn=="Hue_1":
            response = requests.post(url1,data=data)
        else:
            response = requests.post(url2,data=data)
        myobj.updateValue()
    def insertDB(self):
        sql="insert into PhilipsHueLight(id, color, saturation, brightness, temperature) values('%s','%d','%d','%d','%d')"%(self.idn,int(self.color),int(self.saturation),int(self.brightness),int(self.temperature))
        dbEntry(sql)
if __name__ == "__main__":
    while(1):
        c= Color("Hue_2")
        data ='10,52,61'
        c.updateValue()
        updateCloud(api1,c.getColor(),c.getSaturation(),c.getBrightness(),c.getTemperature())
        print(time.ctime(),c.getColor(),c.getSaturation(),c.getBrightness(),c.getTemperature())
        c.postData(data)
        c.insertDB()
        updateCloud(api1,c.getColor(),c.getSaturation(),c.getBrightness(),c.getTemperature())
        c= Color("Hue_1")
        c.updateValue()
        updateCloud(api2,c.getColor(),c.getSaturation(),c.getBrightness(),c.getTemperature())
        print(time.ctime(),c.getColor(),c.getSaturation(),c.getBrightness(),c.getTemperature())
        c.postData(data)
        c.insertDB()
        updateCloud(api2,c.getColor(),c.getSaturation(),c.getBrightness(),c.getTemperature())
