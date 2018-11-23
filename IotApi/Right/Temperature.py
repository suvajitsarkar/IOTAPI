import requests
class Temperature:
    def __init__(myobj):
        myobj.fetchData()
    def getTemperature(myobj):
        return myobj.temp
    def fetchData(myobj):
        url = 'http://192.168.0.4:8080/rest/items/HueColorLamp3_ColorTemperature/state'
        data = ''
        response = requests.get(url, data=data)
        myobj.temp = response.text
