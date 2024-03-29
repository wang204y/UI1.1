# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Mon Jun 10 16:05:18 2019
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QMovie
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 30, 271, 41))
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setStyleSheet("font: 20pt \"宋体\";")
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 271, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/aaa/resource/logo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 530, 161, 31))
        self.label_5.setAutoFillBackground(True)
        self.label_5.setStyleSheet("font: 12pt \"8514oem\";")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 530, 151, 31))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 530, 71, 31))
        self.label_7.setText("")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setPixmap(QtGui.QPixmap(":/aaa/resource/tclogo.JPG"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 80, 231, 16))
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 230, 201, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)   #设置lineEdit的Echomode为密码模式
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(190, 400, 266, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.button1)            #按钮点击信号连接button1槽函数
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.button2)          #按钮点击信号连接button2槽函数
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.label_3.setBuddy(self.lineEdit)
        self.label_4.setBuddy(self.lineEdit_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "易膜设计系统软件"))
        self.label_5.setToolTip(_translate("MainWindow", "这是一个链接"))
        self.label_5.setText(_translate("MainWindow", "<a href=\'http://www.e-mem.cn/cn/index.asp\'>请访问易膜主页</a>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"http://www.hztianchuang.com\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">请访问天创主页</span></a></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "E-MEM Design System v0.0.1"))
        self.label_3.setText(_translate("MainWindow", "用户名"))
        self.label_4.setText(_translate("MainWindow", "密码"))

        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "游客访问"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))

    def button1(self):
        if  self.lineEdit.text() == 'admin' and  self.lineEdit_2.text() == 'tc123456':
            os.system("python emss0726.py")

        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            dialog = QtWidgets.QDialog()  #建立对话框
            dialog.setWindowTitle('提示')
            button = QtWidgets.QPushButton('密码错误请重试',dialog)
            button.clicked.connect(dialog.close)
            button.move(60,30)
            dialog.setWindowModality(QtCore.Qt.ApplicationModal)#弹出对话框时主界面不起作用
            dialog.exec()

    def button2(self):
        dialog = QtWidgets.QDialog()  # 建立对话框
        dialog.setWindowTitle('提示')
        dialog.setFixedSize(800,600)
        laber = QtWidgets.QLabel('', dialog)
        laber.move(50, 50)
        laber.setAlignment(QtCore.Qt.AlignCenter)
        # setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint)
        movie = QMovie('./resource/电渗析.gif')
        laber.setMovie(movie)
        movie.start()
        dialog.exec()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)  #启动qt应用
    myDlg = QMainWindow()           #创建窗口类型实例
    myUI = Ui_MainWindow()          # 创建Ui界面的实例
    myUI.setupUi(myDlg)             #将ui界面实例装在进窗口
    myDlg.show()                    #展示窗口
    sys.exit(myapp.exec_())         #系统循环