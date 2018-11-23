import serial
from xbee import ZigBee
def readdata():
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
        print(adc0,adc1,dio2)
        if(adc0>0):
                s1=(3.3*adc0)/1023
                s1=(s1*1000-500)/100
        #print(int(str(a),16),int(str(b),16),c)
        print("Temperature ",s1)
    except Exception as e:
        print(e," Hello")
while(1):
    readdata()
