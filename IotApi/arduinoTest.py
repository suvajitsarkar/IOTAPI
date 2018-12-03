from Arduino import *
from Xbee import *
from Right import *
d=Dht("DHT_1")
m1=Mq2("MQ2_1")
m2=Mq135("MQ135_1")
x1=xbee1("Xbee_1")
p1=Color("Hue_1")
p2=Color("Hue_2")
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
        p1.updateValue()
        p1.insertDB()
        p2.updateValue()
        p2.insertDB()
    except Exception as e:
        print(e)
