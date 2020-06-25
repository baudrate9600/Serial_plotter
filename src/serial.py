import ctypes 
import os 

#Retrieve C implementation of the UART 
dir_path = os.path.dirname(os.path.abspath(__file__))
so_name = "libserial.so"
so_path = os.path.dirname(dir_path) + os.path.sep + "lib" + os.path.sep + so_name  
serial = ctypes.CDLL(so_path)
serial.read_port.restype = ctypes.POINTER(ctypes.c_char)

#Open the COM port 
def open_port(COM):
    
    #windows wants it strings like this 
    com_str = "\\\\.\\" + COM; 

    #translate to char*
    c_com_str = com_str.encode()
    #Open the port  
    status = serial.open_port(c_com_str)
    if status == -1:
        print("Couldn't open " + COM + "!\n") 
        return -1 
    else:
        print("Succesfully opened " + COM) 
    
#Configure the UART settings 
def conf_port(baudrate=9600,byte_size = 8, stop_bit = 0, parity_bit = 0):
    serial.conf_port(baudrate, byte_size, stop_bit, parity_bit)
    

#Set timouts 
def set_timeouts():
    serial.set_timeouts();

#Write to the serial port 
def write(data):
    c_data_str = data.encode();
    serial.write_port(c_data_str)

#Read from the serial port 
def read():
    status = serial.read_port()
    return status 
    

