import time
import serial
while 1:
    var = int(input("enter number: "))
    if var == 1:
        ser = serial.Serial('/dev/ttyUSB0', timeout=1)
        print(ser.name)
    else:
        ser = serial.Serial('/dev/ttyUSB1')
        print(ser.name)
    xd = str(input("enter a number: ")).encode('utf-8')
    ser.write(xd + b'\n')
    if int(xd.decode('utf-8')) == 1:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    ser.close()
