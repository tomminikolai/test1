import serial
while 1:
    var = int(input("enter number: "))
    if var == 1:
        ser = serial.Serial('dev/tty/')
        print(ser.name)
    else:
        ser = serial.Serial('COM7')
        print(ser.name)
    xd = str(input("enter a number: ")).encode('utf-8')
    ser.write(xd + b'\n')
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    ser.close()
