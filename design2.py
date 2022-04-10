# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'light_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(QtWidgets.QMainWindow):
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
        MainWindow.setStyleSheet("background-color: #F4F5F7;")
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
        self.label.setStyleSheet("background-color: #FFFFFF;\n"
"color: #000000;\n"
"border-radius: 11px")
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#FFFFFF;\n"
"color: #000000;\n"
"border-radius: 11px")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 160, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: #FFFFFF;\n"
"color: #000000;\n"
"border-radius: 11px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 210, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: #FFFFFF;\n"
"color: #000000;\n"
"border-radius: 11px")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 260, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: #FFFFFF;\n"
"color: #00000;\n"
"border-radius: 11px")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(220, 430, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: black;")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #FFFFFF;\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"border-radius: 7px;\n"
"color: #0")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushed)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(430, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #FFFFFF;\n"
"color: #0;\n"
"border-radius: 11px")
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-10, 406, 621, 20))
        self.label_3.setStyleSheet("color: #000000;")
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 0, 16, 421))
        self.line.setStyleSheet("border-left: 1px solid #000000;\n"
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
        self.label_9.setStyleSheet("background-color: #FFFFFF;\n"
"color: silver;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 130, 121, 20))
        self.label_10.setStyleSheet("background-color:#FFFFFF;\n"
"color: silver;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 180, 121, 20))
        self.label_11.setStyleSheet("background-color: #FFFFFF;\n"
"color: silver;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(470, 230, 121, 20))
        self.label_14.setStyleSheet("background-color: #FFFFFF;\n"
"color: silver;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(470, 280, 121, 20))
        self.label_15.setStyleSheet("background-color:#FFFFFF;\n"
"color: silver;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(470, 330, 121, 20))
        self.label_16.setStyleSheet("background-color: #FFFFFF;\n"
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
        self.pushButton.setText(_translate("MainWindow", "Тёмная тема"))
        self.label_13.setText(_translate("MainWindow", "  Водоизмещение:\n"
""))
        self.label_3.setText(_translate("MainWindow", "_________________________________________________________________________________________________________"))
        self.label_8.setText(_translate("MainWindow", "ПОЛИТЕХ"))

    def pushed(self):
        self.hide()
        super(Ui_MainWindow, self).__init__() 
        uic.loadUi('design.ui', self)
        self.show() 
import darkmode_rc
import pic_rc
import sys
if __name__ == '__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
#app = QtWidgets.QApplication(sys.argv)
# = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#MainWindow.show()
#app.exec_()