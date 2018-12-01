import requests
url1 = 'http://192.168.0.4:8080/rest/items/Color1/'
url2 = 'http://192.168.0.4:8080/rest/items/HueColorLamp3_Color/'
url3 = 'http://192.168.0.4:8080/rest/items/HueColorLamp3_ColorTemperature/state'
url4 = 'http://192.168.0.4:8080/rest/items/HueColorLamp1_ColorTemperature/state'
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
        myobj.color=x[0]
        myobj.saturation= x[1]
        myobj.brightness = x[2]
        myobj.temperature = response_t.text
    def postData(myobj):
        data ='142,52,61'
        if myobj.idn==1:
            response = requests.post(url1,data=data)
        else:
            response = requests.post(url2,data=data)
        myobj.fetchData()
c= Color("Hue_2")
c.updateValue()
print(c.getColor(),c.getBrightness(),c.getTemperature())
