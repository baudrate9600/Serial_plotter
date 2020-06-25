import serial as ser 
import ctypes 

ser.open_port("COM4")
ser.conf_port(baudrate=9600) 
ser.set_timeouts()

while 1 > 0 :
    s,num = ser.read()
    #print(s)
    #print(num)
    if num > 0:
        #print (repr(ctypes.cast(s, ctypes.c_char_p).value))
        print(num,s.raw)


