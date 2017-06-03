#!/usr/bin/python3
# -*- coding: utf-8 -*-



import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QListWidget, QStackedWidget, 
                             QLabel, QHBoxLayout, QVBoxLayout)



class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.list = QListWidget(self)
        self.list.insertItem(0, "IP格式转换")
        self.list.insertItem(1, "JSON格式化")
        self.list.setFixedWidth(100)
        
        self.ip_convert = QLabel("IP 转换处理逻辑")
        self.json_format = QLabel("JSON 格式化处理逻辑")
        
        self.stack = QStackedWidget(self)
        self.stack.insertWidget(0, self.ip_convert)
        self.stack.insertWidget(1, self.json_format)
        
        self.list.currentRowChanged.connect(self.stack.setCurrentIndex)
        
        mainLayout = QHBoxLayout(self)
        mainLayout.addWidget(self.list)
        mainLayout.addWidget(self.stack)
        mainLayout.addStretch()
        self.setLayout(mainLayout)
        
        
        self.show()
        
   
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())