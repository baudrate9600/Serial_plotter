import ctypes 
import os 

#Retrieve C implementation of the UART 
dir_path = os.path.dirname(os.path.abspath(__file__))
so_name = "libserial.so"
so_path = os.path.dirname(dir_path) + os.path.sep + "lib" + os.path.sep + so_name  
serial = ctypes.CDLL(so_path)

#Open the COM port 
def open_port(COM):
    
    #windows wants it strings like this 
    com_str = "\\\\.\\" + COM; 

    #translate to char*
    c_com_str = com_str.encode()
    #Open the port  
    status = serial.open_port(c_com_str)
    if status == -1: 
        return -1 
    else:
        return 0
    
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
#..This function returns the string and the amount of bytes
s = ctypes.create_string_buffer(32)
def read(size=32):
    num = serial.read_port(s,size)
    return s,num;
   
def close():
    serial.close_port()

