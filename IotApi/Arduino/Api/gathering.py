import serial
def gatherString():
	ser=serial.Serial("/dev/ttyUSB0",115200)
	ser.baudrate=115200
        return ser.readline()[1:]

