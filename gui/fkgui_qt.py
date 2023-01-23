# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fkgui_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1151, 725)
        MainWindow.setWindowOpacity(0.9)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.hslider1 = QtWidgets.QSlider(self.centralwidget)
        self.hslider1.setGeometry(QtCore.QRect(760, 150, 271, 22))
        self.hslider1.setMinimum(0)
        self.hslider1.setMaximum(180)
        self.hslider1.setSingleStep(1)
        self.hslider1.setProperty("value", 90)
        self.hslider1.setOrientation(QtCore.Qt.Horizontal)
        self.hslider1.setObjectName("hslider1")
        self.hslider2 = QtWidgets.QSlider(self.centralwidget)
        self.hslider2.setGeometry(QtCore.QRect(760, 210, 271, 22))
        self.hslider2.setMinimum(-90)
        self.hslider2.setMaximum(90)
        self.hslider2.setProperty("value", 60)
        self.hslider2.setOrientation(QtCore.Qt.Horizontal)
        self.hslider2.setObjectName("hslider2")
        self.hslider3 = QtWidgets.QSlider(self.centralwidget)
        self.hslider3.setGeometry(QtCore.QRect(760, 270, 271, 22))
        self.hslider3.setMinimum(-90)
        self.hslider3.setMaximum(90)
        self.hslider3.setProperty("value", -60)
        self.hslider3.setOrientation(QtCore.Qt.Horizontal)
        self.hslider3.setObjectName("hslider3")
        self.labels1 = QtWidgets.QLabel(self.centralwidget)
        self.labels1.setGeometry(QtCore.QRect(640, 150, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labels1.setFont(font)
        self.labels1.setStyleSheet("color:rgba(255,255,255,210)")
        self.labels1.setObjectName("labels1")
        self.labels2 = QtWidgets.QLabel(self.centralwidget)
        self.labels2.setGeometry(QtCore.QRect(640, 210, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labels2.setFont(font)
        self.labels2.setStyleSheet("color:rgba(255,255,255,210)")
        self.labels2.setObjectName("labels2")
        self.labels3 = QtWidgets.QLabel(self.centralwidget)
        self.labels3.setGeometry(QtCore.QRect(640, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labels3.setFont(font)
        self.labels3.setStyleSheet("color:rgba(255,255,255,210)")
        self.labels3.setObjectName("labels3")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(780, 500, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setStyleSheet("QPushButton#pushButton_reset{\n"
"background-color: rgb(244, 252, 255);\n"
"border-radius:10px;}\n"
"\n"
"QPushButton#pushButton_reset:pressed{\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius:10px;}")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.hslider4 = QtWidgets.QSlider(self.centralwidget)
        self.hslider4.setGeometry(QtCore.QRect(760, 330, 271, 22))
        self.hslider4.setMinimum(-90)
        self.hslider4.setMaximum(90)
        self.hslider4.setProperty("value", -60)
        self.hslider4.setOrientation(QtCore.Qt.Horizontal)
        self.hslider4.setObjectName("hslider4")
        self.labels4 = QtWidgets.QLabel(self.centralwidget)
        self.labels4.setGeometry(QtCore.QRect(640, 330, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labels4.setFont(font)
        self.labels4.setStyleSheet("color:rgba(255,255,255,210)")
        self.labels4.setObjectName("labels4")
        self.hslider5 = QtWidgets.QSlider(self.centralwidget)
        self.hslider5.setGeometry(QtCore.QRect(760, 390, 271, 22))
        self.hslider5.setMinimum(-90)
        self.hslider5.setMaximum(90)
        self.hslider5.setProperty("value", -60)
        self.hslider5.setOrientation(QtCore.Qt.Horizontal)
        self.hslider5.setObjectName("hslider5")
        self.hslider6 = QtWidgets.QSlider(self.centralwidget)
        self.hslider6.setGeometry(QtCore.QRect(760, 450, 271, 22))
        self.hslider6.setMinimum(-90)
        self.hslider6.setMaximum(90)
        self.hslider6.setProperty("value", -60)
        self.hslider6.setOrientation(QtCore.Qt.Horizontal)
        self.hslider6.setObjectName("hslider6")
        self.labels6 = QtWidgets.QLabel(self.centralwidget)
        self.labels6.setGeometry(QtCore.QRect(640, 450, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labels6.setFont(font)
        self.labels6.setStyleSheet("color:rgba(255,255,255,210)")
        self.labels6.setObjectName("labels6")
        self.labels5 = QtWidgets.QLabel(self.centralwidget)
        self.labels5.setGeometry(QtCore.QRect(640, 390, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labels5.setFont(font)
        self.labels5.setStyleSheet("color:rgba(255,255,255,210)")
        self.labels5.setObjectName("labels5")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 10, 1131, 700))
        self.background.setStyleSheet("border-image: url(:/images/background.jpg);\n"
"border-radius: 24px;")
        self.background.setObjectName("background")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(830, 650, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:rgba(255,255,255,210)")
        self.label1.setObjectName("label1")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(420, 640, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton#pushButton1{\n"
"background-color: rgb(244, 252, 255);\n"
"border-radius:5px;}\n"
"\n"
"QPushButton#pushButton1:pressed{\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius:5px;}")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(510, 640, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setAutoFillBackground(False)
        self.pushButton2.setStyleSheet("QPushButton#pushButton2{\n"
"background-color: rgb(244, 252, 255);\n"
"border-radius:5px;}\n"
"\n"
"\n"
"QPushButton#pushButton2:pressed{\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius:5px;}")
        self.pushButton2.setObjectName("pushButton2")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(280, 40, 661, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setAutoFillBackground(False)
        self.label1_2.setStyleSheet("color:rgba(255,255,255,210)")
        self.label1_2.setObjectName("label1_2")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setEnabled(True)
        self.MplWidget.setGeometry(QtCore.QRect(90, 120, 500, 500))
        self.MplWidget.setMouseTracking(True)
        self.MplWidget.setTabletTracking(True)
        self.MplWidget.setAutoFillBackground(False)
        self.MplWidget.setStyleSheet("border-radius: 24px;\n"
"background-color: rgba(255,255,255,0.5);")
        self.MplWidget.setObjectName("MplWidget")
        self.background.raise_()
        self.hslider1.raise_()
        self.hslider2.raise_()
        self.hslider3.raise_()
        self.labels1.raise_()
        self.labels2.raise_()
        self.labels3.raise_()
        self.pushButton_reset.raise_()
        self.hslider4.raise_()
        self.labels4.raise_()
        self.hslider5.raise_()
        self.hslider6.raise_()
        self.labels6.raise_()
        self.labels5.raise_()
        self.label1.raise_()
        self.pushButton1.raise_()
        self.pushButton2.raise_()
        self.label1_2.raise_()
        self.MplWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labels1.setText(_translate("MainWindow", "Joint 1:"))
        self.labels2.setText(_translate("MainWindow", "Joint 2 :"))
        self.labels3.setText(_translate("MainWindow", "Joint 3 :"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.labels4.setText(_translate("MainWindow", "Joint 4 :"))
        self.labels6.setText(_translate("MainWindow", "Joint 6 :"))
        self.labels5.setText(_translate("MainWindow", "Joint 5 :"))
        self.label1.setText(_translate("MainWindow", "By David Quezada"))
        self.pushButton1.setText(_translate("MainWindow", "FRONT"))
        self.pushButton2.setText(_translate("MainWindow", "TOP"))
        self.label1_2.setText(_translate("MainWindow", "FORWARD KINEMATICS 6DoF GUI"))
from mplwidget import MplWidget
import res
