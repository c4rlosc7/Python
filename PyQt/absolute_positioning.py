#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
labels using absolute positioning. 
"""

import sys
from PyQt4.QtGui import *

class Window(QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.startUI()
        
    def startUI(self):
        
        label1 = QLabel('Label 1', self)
        label1.move(10, 10)

        label2 = QLabel('Label 2', self)
        label2.move(50, 50)
        
        label3 = QLabel('Label 3', self)
        label3.move(90, 90)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute positioning')    
        self.show()
        
def main():
    
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
