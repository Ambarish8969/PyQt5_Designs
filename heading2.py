# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heading.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 141, 431))
        self.frame.setStyleSheet("background-color: rgb(167, 167, 167);\n"
                                 "color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setGeometry(QtCore.QRect(0, 10, 131, 401))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 131, 339))
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 0, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_2.setObjectName("label_2")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 131, 339))
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_4.setObjectName("label_4")
        self.toolBox.addItem(self.page_2, "")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 430, 1041, 121))
        self.frame_2.setStyleSheet("background-color: rgb(116, 116, 116);\n"
                                   "color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(140, 0, 881, 431))
        self.frame_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(238, 236, 220);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSettings = QtWidgets.QMenu(self.menuTools)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste_2 = QtWidgets.QAction(MainWindow)
        self.actionPaste_2.setObjectName("actionPaste_2")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImpot = QtWidgets.QAction(MainWindow)
        self.actionImpot.setObjectName("actionImpot")
        self.actionRecent_Files = QtWidgets.QAction(MainWindow)
        self.actionRecent_Files.setObjectName("actionRecent_Files")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDisplay_Settings = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Settings.setObjectName("actionDisplay_Settings")
        self.actionFont_Settings = QtWidgets.QAction(MainWindow)
        self.actionFont_Settings.setObjectName("actionFont_Settings")
        self.actionWindow_Setting = QtWidgets.QAction(MainWindow)
        self.actionWindow_Setting.setObjectName("actionWindow_Setting")
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "PySide_icons/blue-document--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "PySide_icons/document-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCopy.setObjectName("actionCopy")
        self.menuFile.addAction(self.actionnew)
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addAction(self.actionclose)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionImpot)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menuEdit.addAction(self.actionDelete)
        self.menuSettings.addAction(self.actionDisplay_Settings)
        self.menuSettings.addAction(self.actionFont_Settings)
        self.menuSettings.addAction(self.actionWindow_Setting)
        self.menuTools.addAction(self.menuSettings.menuAction())
        self.menuTools.addAction(self.actionNew_Window)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionCopy)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionopen.triggered.connect(self.browse)
        self.actionnew.triggered.connect(self.newwin)

    def newwin(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def browse(self):
        path = QFileDialog.getOpenFileName(None, 'Open a file', '','All Files (*.*)')
        if path != ('', ''):
            print("File path : "+ path[0])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATSSL"))
        self.label.setText(_translate("MainWindow", "Hello.py"))
        self.label_2.setText(_translate("MainWindow", "Views.py"))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.page), _translate("MainWindow", "Folder_1"))
        self.label_3.setText(_translate("MainWindow", "index.html"))
        self.label_4.setText(_translate("MainWindow", "index.css"))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.page_2), _translate("MainWindow", "Folder_2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnew.setText(_translate("MainWindow", "New Window"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionopen.setText(_translate("MainWindow", "Open"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionclose.setText(_translate("MainWindow", "Close"))
        self.actionclose.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste_2.setText(_translate("MainWindow", "Paste"))
        self.actionPaste_2.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionDocumentation.setText(
            _translate("MainWindow", "Documentation"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImpot.setText(_translate("MainWindow", "Import"))
        self.actionRecent_Files.setText(
            _translate("MainWindow", "Recent Files"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionDisplay_Settings.setText(
            _translate("MainWindow", "Display Settings"))
        self.actionFont_Settings.setText(
            _translate("MainWindow", "Font Settings"))
        self.actionWindow_Setting.setText(
            _translate("MainWindow", "Window Setting"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
