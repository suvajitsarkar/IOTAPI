from Arduino import *
from Xbee1 import *
d=Dht("DHT1")
m1=Mq2("MQ2_1")
m2=Mq135("MQ135_1")
x1=xbee1("Xbee_1")
while 1:
    try:
        d.updateValue()
        d.insertDB()
        m1.updateValue()
        m1.insertDB()
        m2.updateValue()
        m2.insertDB()
        x1.updateValue()
        x1.insertDB()
    except Exception as e:
        print(e)
