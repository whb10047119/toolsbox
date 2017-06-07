#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from toolsbox_ui import Ui_toolsbox
import ipaddress
import json

class MyFirstGuiProgram(Ui_toolsbox):
    def __init__(self, dialog):
        Ui_toolsbox.__init__(self)
        self.setupUi(dialog)
        self.ipconvert_str2num_run.clicked.connect(self.ipconvert_str2num_proc)
        self.ipconvert_num2str_run.clicked.connect(self.ipconvert_num2str_proc)
        self.jsonformat_run.clicked.connect(self.jsonformat_proc)
    
    def ipconvert_num2str_proc(self):
        numip = self.ipconvert_num2str_input.text()
        strip = ipaddress.ip_address(int(numip))
        print(strip)
        self.ipconvert_num2str_output.setText(str(strip))
        
    def ipconvert_str2num_proc(self):
        strip = self.ipconvert_str2num_input.text()
        numip = int(ipaddress.ip_address(strip))
        self.ipconvert_str2num_output.setText(str(numip))
        
    def jsonformat_proc(self):
        text = self.jsonformat_text.toPlainText()
        json_obj = json.loads(text)
        text = json.dumps(json_obj, indent=4)
        self.jsonformat_text.setPlainText(text)
        
        
        
    
    
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    
    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())