from os import kill
from PyQt5 import QtCore, QtGui, QtWidgets
from socket import AF_INET, SOCK_STREAM
import socket 


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 625)
        Form.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.pbConnect = QtWidgets.QPushButton(Form,clicked=lambda:self.con())
        self.pbConnect.setGeometry(QtCore.QRect(340, 260,600, 81))
        self.pbConnect.setStyleSheet("font: 75 20pt \"Arial\";")
        self.pbConnect.setObjectName("pbConnect")
        # self.pbsend = QtWidgets.QPushButton(Form,clicked=lambda:self.send())
        # self.pbsend.setGeometry(QtCore.QRect(950, 160,200, 81))
        # self.pbsend.setStyleSheet("font: 75 20pt \"Arial\";")
        # self.pbsend.setObjectName("pbsend")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(340, 160,600, 81))
        self.lineEdit.setStyleSheet("\n"
"font: 75 16pt \"Arial\";")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
  
            
    def con(self):
        
        c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c.connect((socket.gethostname(),1234))
        msg = c.recv(1024)
        self.pbConnect.setText(msg.decode("utf-8")) 
        k=self.lineEdit.text()
        c.send(bytes(k,'utf-8'))   
        
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbConnect.setText(_translate("Form", "Connect"))
        # self.pbsend.setText(_translate("Form", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())