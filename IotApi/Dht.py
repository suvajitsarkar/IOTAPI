import serial
ser=serial.Serial("/dev/ttyUSB0",115200)
ser.baudrate=115200
while(1):
    read_ser=ser.readline()
    print(read_ser)
