import serial
lmao = int(input("enter number: "))
if lmao > 0:
    ser1 = serial.Serial('/dev/ttyUSB0')
    print(ser1.name)
if lmao > 1:
    ser2 = serial.Serial('/dev/ttyUSB1')
    print(ser2.name)
while 1:
    var = int(input("enter number: "))
    xd = str(input("enter a number: ")).encode('utf-8')
    if var == 1:
        ser1.write(xd + b'\n')
        if int(xd.decode('utf-8')) == 1 or int(xd.decode('utf-8')) == 0:
            line = ser1.readline().decode('utf-8').rstrip()
    if var == 2:
        ser2.write(xd + b'\n')
        if int(xd.decode('utf-8')) == 1:
            line = ser2.readline().decode('utf-8').rstrip()
    print(line)
