
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap
import asyncio
import time
import threading
import sqlite3
from ai import predict
import time
import matplotlib.pyplot as plt
from text_finder import finder
import cv2
import datetime
from main import camera_start


from design2 import Ui_MainWindow

class Main():
        def run(self, other):
                other.hide()
                #MainWindow = QtWidgets.QMainWindow()
                #ui = Ui_MainWindow2()
                #ui.setupUi(MainWindow)
                self.show()

class Ui_MainWindow1(QtWidgets.QMainWindow, Main):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 468)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #1A1125;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 10, 42, 36))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/draw.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 60, 171, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: #ba66ff;\n"
"border-radius: 11px")
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: #ba66ff;\n"
"border-radius: 11px")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 160, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: #ba66ff;\n"
"border-radius: 11px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 210, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: #ba66ff;\n"
"border-radius: 11px")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 260, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: #ba66ff;\n"
"border-radius: 11px")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(220, 430, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        #self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton1.setGeometry(QtCore.QRect(450, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        #self.pushButton1.setFont(font)
        #self.pushButton1.setStyleSheet("background-color: rgb(38, 29, 50);\n"
#"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
#"border-radius: 7px;\n"
#"color: #ba66ff")
        #self.pushButton1.setObjectName("pushButton")
        #self.pushButton1.clicked.connect(self.pushed)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(430, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: #ba66ff;\n"
"border-radius: 11px")
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, 406, 621, 20))
        self.label_3.setStyleSheet("color: #ba66ff;")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 0, 16, 421))
        self.line.setStyleSheet("border-left: 1px solid #ba66ff;\n"
"border-style: inset;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 10, 126, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(7)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(55, 179, 74);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 80, 121, 20))
        self.label_9.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: silver;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 130, 121, 20))
        self.label_10.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: silver;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 180, 121, 20))
        self.label_11.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: silver;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(470, 230, 121, 20))
        self.label_14.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: silver;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(470, 280, 121, 20))
        self.label_15.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: silver;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(470, 330, 121, 20))
        self.label_16.setStyleSheet("background-color: rgb(38, 29, 50);\n"
"color: silver;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        cap = cv2.VideoCapture(0)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/снимок-removebg-preview.BQmcL.png\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "  Идентификатор: \n"
" "))
        self.label_4.setText(_translate("MainWindow", "  Название:\n"
" "))
        self.label_5.setText(_translate("MainWindow", "  Позывной:\n"
""))
        self.label_6.setText(_translate("MainWindow", "  Тип:\n"
""))
        self.label_7.setText(_translate("MainWindow", "  Размеры:\n"
""))
        self.label_12.setText(_translate("MainWindow", "Copyright 2022 - All Rights Reserved"))
        #self.pushButton1.setText(_translate("MainWindow", "Светлая тема"))
        self.label_13.setText(_translate("MainWindow", "  Водоизмещение:\n"
""))
        self.label_3.setText(_translate("MainWindow", "_________________________________________________________________________________________________________"))
        self.label_8.setText(_translate("MainWindow", "ПОЛИТЕХ"))
        self.label_144 = QtWidgets.QLabel(self.centralwidget)
        self.label_144.setGeometry(QtCore.QRect(0, 0, 410, 420))
        self.my_timer1 = QtCore.QTimer()
        self.my_timer1.timeout.connect(self.lexa_pidor)
        self.my_timer1.start(5000)
        self.pushed()
        self.ai_start(cap)
        self.my_timer2 = QtCore.QTimer()
        self.my_timer2.timeout.connect(lambda: self.load_in_sql())
        self.my_timer2.start(10000)
        self.my_timer = QtCore.QTimer()
        self.my_timer.timeout.connect(lambda: self.ai_start(cap))
        self.my_timer.start(100)
        
    def pushed(self):
        self.lexa_pidor()
    def ai_start(self, cap):
        camera_start(cap)
        #hbox = QtWidgets.QHBoxLayout(self)
        pixmap = QPixmap("cam.png")
        self.label_144.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        predict('cam.png')
        self.update()
        
    def lexa_pidor(self):
        f = open('text.txt').read().splitlines()
        self.label_9.setText(f[0])
        self.label_10.setText(f[1])
        self.label_11.setText(f[2])
        self.label_14.setText(f[3])
        self.label_15.setText(f[4])
        self.label_16.setText(f[5])
        self.update()
    def load_in_sql(self):
        f = open('text.txt').read().splitlines()
        now = datetime.datetime.now()
        cur.execute(f"""
        INSERT INTO users(Identifier, MName,
        FName, Type, Size, Displacement, Time) 
        VALUES('{f[0]}', '{f[1]}', '{f[2]}', '{f[3]}', '{f[4]}', '{f[5]}', '{str(now)}');
        """)
        conn.commit()



import darkmode_rc
import pic_rc

import os

conn = sqlite3.connect('ships.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
Identifier TEXT,
MName TEXT,
FName TEXT,
Type TEXT,
Size TEXT,
Displacement TEXT,
Time TEXT);
""")
conn.commit()

#if __name__ == '__main__':
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow1()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())