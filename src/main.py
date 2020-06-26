#Serial module 
import serial as ser 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon 
import ctypes 

ser.open_port("COM4")
ser.conf_port(baudrate=9600) 
ser.set_timeouts()

x = np.linspace(0,2,100)
y = np.linspace(0,2,100)

#QT5 
matplotlib.use('Qt5Agg')

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self): 
        self.setGeometry(300, 300, 300, 220) 
        self.setWindowTitle('Icon') 
        self.setWindowIcon(QIcon('..\lib\serial.png'))
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
