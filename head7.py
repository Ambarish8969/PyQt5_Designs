# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heading.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QPushButton
import xml.etree.ElementTree as et
import itertools as it
import xml.dom.minidom as minidom


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 611)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 131, 291))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(4, 10, 111, 31))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 250, 101, 28))
        self.pushButton_5.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 10, 881, 291))
        self.frame_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(212, 10, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 10, 131, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 10, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 40, 361, 108))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setGeometry(QtCore.QRect(220, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 201, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 80, 141, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(210, 40, 151, 91))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(10, 220, 351, 80))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 20, 171, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 20, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_2)
        self.treeWidget.setGeometry(QtCore.QRect(510, 50, 256, 192))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 290, 1021, 41))
        self.frame_3.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 55, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 10, 171, 22))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 330, 1031, 41))
        self.frame_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(214, 214, 214);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(480, 10, 55, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 370, 1011, 161))
        self.frame_5.setStyleSheet("background-color: rgb(238, 226, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 26))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#...........................................................................................................
        self.actionOpen.triggered.connect(self.browse)
        self.actionNew.triggered.connect(self.newwin)
        self.listWidget.close()
        self.pushButton_2.clicked.connect(self.diagn_clicked)
        self.frame_6.close()
        self.frame_7.close()
        self.label_4.close()
        self.treeWidget.close()
        self.listWidget.itemDoubleClicked.connect(self.getitem)
        self.pushButton.clicked.connect(self.browse)
        self.pushButton_6.clicked.connect(self.time_show)
        self.comboBox_2.currentIndexChanged.connect(self.press)
        self.treeWidget.itemClicked.connect(self.onItemClicked)
        self.lineEdit.textChanged[str].connect(self.convert_to_xml)
        self.listopen=False

    #function for Opening the file........
    def browse(self):    
        path = QFileDialog.getOpenFileName(None, 'Open a file', '','All Files (*.*)')
        url=QtCore.QUrl.fromLocalFile(path)
        self.lineEdit.setText(str(url.fileName()))
        if path != ('', ''):
            print("File path : "+ path[0])   
    
    #Function for converting text file to xml file.......
    def convert_to_xml(self,path):
        root = et.Element('File_Name')
        with open(path) as f:
            lines = f.read().splitlines()
        celldata = et.SubElement(root, 'FileData')
        for line in it.groupby(lines):
            line=line[0]
            if not line:
                celldata = et.SubElement(root, 'FileData')
            else:
                tag = line.split(":")
                el=et.SubElement(celldata,tag[0].replace(" ",""))
                tag=' '.join(tag[1:]).strip()
                if 'File Name' in line:
                    tag = line.split("\\")[-1].strip()
                elif 'File Size' in line:
                    splist =  filter(None,line.split(" "))
                    tag = splist[splist.index('Low:')+1]
                    #splist[splist.index('High:')+1]
                el.text = tag
        formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ",encoding='utf-8').strip()
        with open("test.xml","wb") as f:
            f.write(formatedXML)
        self.treeWidget.show()

        #Reading the file...........
        f=open("test.xml","r").read()
        self.printtree(f)

    #When treewidget item clicked.............
    def onItemClicked(self):
        item=self.treeWidget.currentItem()
        print(item.text(0))

    def printtree(self,s):
        tree=et.fromstring(s)
        self.treeWidget.setColumnCount(1)
        a=QtWidgets.QTreeWidgetItem([tree.tag])
        self.treeWidget.addTopLevelItem(a)

        def displaytree(a,s):
            for child in s:
                branch=QtWidgets.QTreeWidgetItem([child.tag])
                a.addChild(branch)
                displaytree(branch,child)
            if s.text is not None:
                content=s.text
                a.addChild(QtWidgets.QTreeWidgetItem([content]))
        displaytree(a,tree)

    #function for Creating New Window........
    def newwin(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    #Function for getting items when listwidget items double clicked......
    def getitem(self):
        selected=self.listWidget.currentRow()
        if str(selected)=="0":
            self.frame_6.show()
            self.frame_7.show()
            self.label_4.show()
            self.listWidget.close()
        else:
            pass
        
    #Action for when diagnostic service clicked........
    def diagn_clicked(self):
        if self.listopen==False:
            self.listWidget.show()
            self.listopen=True
        else:
            self.listWidget.close()
            self.listopen=False
    
    #Function for system time............
    def time_show(self):
        currentTime=QtCore.QTime.currentTime()
        time=currentTime.toString()
        self.lineEdit_3.setText(str(time))
        print(time)

    #Function for browsing the files.........
    def browse(self):
        filename = QFileDialog.getOpenFileName(None, "Open File", "")
        self.lineEdit.setText(filename[0])

    #Function for Selecting Combobox Items...........
    def press(self):
        select=self.comboBox_2.currentText()
        data=['Hard','Soft']
        print(select)
        if select=="Hard Reset":
            self.lineEdit_2.setText(str(len(data))+str(" 11 01"))
        elif(select=="Soft Reset"):
            self.lineEdit_2.setText(str(len(data))+str(" 11 02"))
        else:
            pass
#............................................................................................................

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATSSL"))
        self.label.setText(_translate("MainWindow", "Select Protocol"))
        self.pushButton_5.setText(_translate("MainWindow", "Connect Button"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Blutooth"))
        self.comboBox.setItemText(1, _translate("MainWindow", "WiFi"))
        self.comboBox.setItemText(2, _translate("MainWindow", "USB"))
        self.pushButton_2.setText(_translate("MainWindow", "Dignostic Service"))
        self.pushButton_3.setText(_translate("MainWindow", "Flash Programming"))
        self.pushButton_4.setText(_translate("MainWindow", "Self Test DIDs"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Hard Reset"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Soft Reset"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "ECU Reset"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Identification"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Security Access"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Session"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Stored Data"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Routine Cotrol"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "ECU Reset"))
        self.pushButton_6.setText(_translate("MainWindow", "Transmit"))
        self.label_2.setText(_translate("MainWindow", "TX"))
        self.label_3.setText(_translate("MainWindow", "RX"))
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
