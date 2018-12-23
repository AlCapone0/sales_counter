import serial

ser = serial.Serial(
    port='COM14',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
line = []

while True:
    for c in ser.read():
        line.append(c)

        print(c)
        #print(chr(c), end="")
        #print(line)

        #if c == 102:
            #print("Line: " + ''.join(line))
            #line = []
            #break

ser.close()