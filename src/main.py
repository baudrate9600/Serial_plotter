import serial as ser 
import ctypes 

ser.open_port("COM4")
ser.conf_port(baudrate=9600) 
ser.set_timeouts()

while 1 > 0 :
    test = ser.read()
    print(test)
    print (repr(ctypes.cast(test, ctypes.c_char_p).value))

