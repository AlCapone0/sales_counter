import serial
import datetime

ser = [0 for i in range(30)]
f = [0 for i in range(30)]

def read_com(port_num):

    try:
        ser[port_num] = serial.Serial('COM'+str(port_num), timeout=0)
        print("connected to COM" + str(port_num) + " " + str(datetime.datetime.now()))
    except serial.SerialException:
        pass
    except TypeError:
        pass

    try:
        dataIn = str(ser[port_num].readline())[2:18]

        if len(dataIn)>=16:
            print('COM' + str(port_num) + ": " + dataIn + " " + str(datetime.datetime.now()))
            f[port_num] = open('filecom' + str(port_num) + '.txt', 'a')
            f[port_num].write(dataIn + " " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n')
            f[port_num].close()

    except serial.SerialException:
        # There is no new data from serial port

        ser[port_num].close()
    except TypeError:
        # Disconnect of USB->UART occured

        ser[port_num].close()
    except NameError:
        ser[port_num].close()

while True:
    #read_com(3)
    read_com(14)
