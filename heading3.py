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
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(320, 180, 171, 61))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_5.setObjectName("label_5")
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
        self.menuSettings_2 = QtWidgets.QMenu(self.menuTools)
        self.menuSettings_2.setObjectName("menuSettings_2")
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
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PySide_icons/icons8-save-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_2.setIcon(icon)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("PySide_icons/icons8-copy-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCopy.setObjectName("actionCopy")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("PySide_icons/icons8-new-file-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy_2 = QtWidgets.QAction(MainWindow)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("PySide_icons/icons8-opened-folder-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImport = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("PySide_icons/icons8-import-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon4)
        self.actionImport.setObjectName("actionImport")
        self.actionExport_2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("PySide_icons/icons8-export-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_2.setIcon(icon5)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionSave_3 = QtWidgets.QAction(MainWindow)
        self.actionSave_3.setIcon(icon)
        self.actionSave_3.setObjectName("actionSave_3")
        self.actionCopy_3 = QtWidgets.QAction(MainWindow)
        self.actionCopy_3.setIcon(icon1)
        self.actionCopy_3.setObjectName("actionCopy_3")
        self.actionDelete_2 = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("PySide_icons/icons8-delete-file-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_2.setIcon(icon6)
        self.actionDelete_2.setObjectName("actionDelete_2")
        self.actionCut_2 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("PySide_icons/icons8-cut-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut_2.setIcon(icon7)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("PySide_icons/icons8-settings-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon8)
        self.actionSettings.setObjectName("actionSettings")
        self.actionDisplay_Settings_2 = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Settings_2.setObjectName("actionDisplay_Settings_2")
        self.actionFont_Settings_2 = QtWidgets.QAction(MainWindow)
        self.actionFont_Settings_2.setObjectName("actionFont_Settings_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExport_2)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addAction(self.actionSave_3)
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menuEdit.addAction(self.actionDelete_2)
        self.menuEdit.addAction(self.actionCopy_3)
        self.menuSettings_2.addAction(self.actionDisplay_Settings_2)
        self.menuSettings_2.addAction(self.actionFont_Settings_2)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuSettings_2.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionSave_2)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionExport_2)
        self.toolBar.addAction(self.actionDelete_2)
        self.toolBar.addAction(self.actionCut_2)
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionOpen.triggered.connect(self.browse)
        self.actionNew.triggered.connect(self.newwin)
        self.actionOpen.triggered.connect(lambda:self.clicked("Open was Clicked."))
        self.actionNew.triggered.connect(lambda:self.clicked("New was Clicked."))
        self.actionExport_2.triggered.connect(lambda:self.clicked("Export was Clicked."))
        self.actionImport.triggered.connect(lambda:self.clicked("Import was Clicked."))
        self.actionSave_3.triggered.connect(lambda:self.clicked("Save was Clicked."))
        self.actionCut_2.triggered.connect(lambda:self.clicked("Cut was Clicked."))
        self.actionOpen.triggered.connect(lambda:self.clicked("Open was Clicked."))



    def newwin(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def browse(self):
        path = QFileDialog.getOpenFileName(None, 'Open a file', '','All Files (*.*)')
        if path != ('', ''):
            print("File path : "+ path[0])

    def clicked(self,text):
        self.label_5.setText(text)
        self.label_5.adjustSize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATSSL"))
        self.label.setText(_translate("MainWindow", "Hello.py"))
        self.label_2.setText(_translate("MainWindow", "Views.py"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Folder_1"))
        self.label_3.setText(_translate("MainWindow", "index.html"))
        self.label_4.setText(_translate("MainWindow", "index.css"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Folder_2"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSettings_2.setTitle(_translate("MainWindow", "Settings"))
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
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImpot.setText(_translate("MainWindow", "Import"))
        self.actionRecent_Files.setText(_translate("MainWindow", "Recent Files"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionDisplay_Settings.setText(_translate("MainWindow", "Display Settings"))
        self.actionFont_Settings.setText(_translate("MainWindow", "Font Settings"))
        self.actionWindow_Setting.setText(_translate("MainWindow", "Window Setting"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCopy_2.setText(_translate("MainWindow", "Copy"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport_2.setText(_translate("MainWindow", "Export"))
        self.actionSave_3.setText(_translate("MainWindow", "Save"))
        self.actionSave_3.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy_3.setText(_translate("MainWindow", "Copy"))
        self.actionCopy_3.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionDelete_2.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_2.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionCut_2.setText(_translate("MainWindow", "Cut"))
        self.actionCut_2.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionDisplay_Settings_2.setText(_translate("MainWindow", "Display Settings"))
        self.actionFont_Settings_2.setText(_translate("MainWindow", "Font Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
