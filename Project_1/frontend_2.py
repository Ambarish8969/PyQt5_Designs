# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
# from tkinter import Text
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox

data_1="0x5555AAAA"
data_2="0x5555BBBB"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 721, 331))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 150, 141, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 100, 91, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.listWidget.setStyleSheet("background-color: rgb(255, 247, 234);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(360, 10, 341, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 291, 41))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.listWidget.itemDoubleClicked.connect(self.open_terminal)
        self.listWidget.itemDoubleClicked.connect(self.show_connection)
        self.pushButton.clicked.connect(self.onClickconnect)
        self.lineEdit.close()
        self.pushButton_2.close()
        # self.pushButton_2.clicked.connect(self.onClickConnectButton)
        self.data="0x5555AAAA"
  
    def onClickconnect(self):
        self.label_2.setText("connected")
        time.sleep(5)
        self.label_2.clear()
        if (data_1==data_1):
            # print("Control is in Application.")
            self.label_2.setText(str("Control is in Application."))
            # Show message box.
            msg=QMessageBox()
            msg.setWindowTitle("Status")
            msg.setText("Control is in Application.  ")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec_()
        else:
            # print("Control is in Boot Loader.")
            self.label_2.setText(str("Control is in BootLoader."))
            msg=QMessageBox()
            msg.setWindowTitle("Status")
            msg.setText("Control is in BootLoader.   ")
            msg.setIcon(QMessageBox.Critical)
            x=msg.exec_()


    # Opening the terminal window after selecting item  in listwidget.
    # def open_terminal(self):
    #     self.window=QtWidgets.QMainWindow()
    #     self.ambi=Ui_MainWindow2()
    #     self.ambi.setupUi(self.window)
    #     self.window.show()
    
    # Show Connection.
    def show_connection(self):
        time.sleep(2)
        self.label_2.setText(str("waiting for the connection...."))

    # Check the data.
    # def onClickConnectButton(self):
    #     if (data_1==data_1):
    #         # print("Control is in Application.")
    #         self.label_2.setText(str("Control is in Application."))
    #         # Show message box.
    #         msg=QMessageBox()
    #         msg.setWindowTitle("Status")
    #         msg.setText("Control is in Application.  ")
    #         msg.setIcon(QMessageBox.Information)
    #         x=msg.exec_()
    #     else:
    #         # print("Control is in Boot Loader.")
    #         self.label_2.setText(str("Control is in BootLoader."))
    #         msg=QMessageBox()
    #         msg.setWindowTitle("Status")
    #         msg.setText("Control is in BootLoader.   ")
    #         msg.setIcon(QMessageBox.Critical)
    #         x=msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Rasbery-pi"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Aurduino"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
