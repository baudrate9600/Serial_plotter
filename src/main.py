#Serial module 
import serial as ser 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.qt_compat import QtCore,QtWidgets,is_pyqt5
from matplotlib.figure import Figure

import numpy as np
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QAction
from PyQt5.QtGui import QIcon 
import ctypes 

ser.open_port("COM4")
ser.conf_port(baudrate=9600) 
ser.set_timeouts()

x = np.linspace(0,2,100)
y = np.linspace(0,2,100)

#QT5 
matplotlib.use('Qt5Agg')


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self): 
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QtWidgets.QVBoxLayout(self.central_widget) 

        canvas = Canvas(self, width=8,height = 4,dpi = 100) 
        layout.addWidget(canvas) 
        self.toolbar = self.addToolBar('Exit')
        #button.move(100,350)
        self.setWindowTitle('Serial Plotter') 
        self.setWindowIcon(QIcon('..\lib\serial.png'))

        self.show()

class Canvas(FigureCanvas):
    def __init__(self,parent = None, width = 5, height = 5,dpi =100):
        fig = Figure(figsize=(width,height),dpi=dpi)
        self.axes = fig.add_subplot(111) 
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        x = np.linspace(0, 2 * np.pi ,50)
        
        ax = self.figure.add_subplot(111) 
        ax.plot(x,np.sin(x),'*-')
        

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
