import serial
import time

arduino = serial.Serial('COM12',9600)
time.sleep(2)
print("ready")
while 1:
    dataUser=input()
    if dataUser =='1':
        arduino.write(b'1')
        print("Ok 1")
    if dataUser =='2':
        arduino.write(b'2')
        print("Ok 2")
    if dataUser =='3':
        arduino.write(b'3')
        print("Ok 3")
    if dataUser =='4':
        arduino.write(b'4')
        print("Ok 4")