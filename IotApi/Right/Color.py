import requests
url = 'http://192.168.0.4:8080/rest/items/Color1/'
class Color:
    def __init__(myobj):
        myobj.fetchData()
    def getColor(myobj):
        return myobj.color
    def getSaturation(myobj):
        return myobj.saturation
    def getBrightness(myobj):
        return myobj.brightness
    def fetchData(myobj):
        data = ''
        response = requests.get(url+'state', data=data)
        x= response.text.split(",")
        myobj.color=x[0]
        myobj.saturation= x[1]
        myobj.brightness = x[2]
    def postData(myobj):
        data ='142,52,61'
        response = requests.post(url,data=data)
        myobj.fetchData()
