# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientfkIGPV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(620, 315)
        MainWindow.setMinimumSize(QSize(620, 315))
        MainWindow.setMaximumSize(QSize(620, 315))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: #37393d")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_for_view = QTextEdit(self.centralwidget)
        self.textEdit_for_view.setObjectName(u"textEdit_for_view")
        self.textEdit_for_view.setGeometry(QRect(12, 10, 311, 211))
        font = QFont()
        font.setFamily(u"Montserrat")
        self.textEdit_for_view.setFont(font)
        self.textEdit_for_view.setStyleSheet(u"background-color: rgb(76, 79, 84);\n"
" color: white;\n"
"border-radius: 1px solid;\n"
"")
        self.lineEdit_for_writetext = QLineEdit(self.centralwidget)
        self.lineEdit_for_writetext.setObjectName(u"lineEdit_for_writetext")
        self.lineEdit_for_writetext.setGeometry(QRect(12, 230, 231, 31))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.lineEdit_for_writetext.setFont(font1)
        self.lineEdit_for_writetext.setStyleSheet(u" background: rgb(76, 79, 84);\n"
" color: white;\n"
"border-radius: 1px solid;")
        self.btn_for_sendmessage = QPushButton(self.centralwidget)
        self.btn_for_sendmessage.setObjectName(u"btn_for_sendmessage")
        self.btn_for_sendmessage.setGeometry(QRect(410, 230, 211, 61))
        self.btn_for_sendmessage.setStyleSheet(u"background: #7fc7ff;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  width: 140px;\n"
"  height: 45px;\n"
"  line-height: 45px;\n"
"  border-radius: 10px;\n"
"  margin: 10px 20px;\n"
"  font-family: 'Montserrat', sans-serif;\n"
"  font-size: 11px;\n"
"  text-transform: uppercase;\n"
"  text-align: center;\n"
"  letter-spacing: 3px;\n"
"  font-weight: 600;\n"
"  color: #524f4e;\n"
"  box-shadow: 0 8px 15px rgba(0, 0, 0, .1);\n"
"  transition: .3s;\n"
"  background: #2EE59D;\n"
"  box-shadow: 0 15px 20px rgba(46, 229, 157, .4);\n"
"  color: white;\n"
"  transform: translateY(-7px);")
        self.comboBox_for_select_topic = QComboBox(self.centralwidget)
        self.comboBox_for_select_topic.setObjectName(u"comboBox_for_select_topic")
        self.comboBox_for_select_topic.setGeometry(QRect(330, 40, 261, 31))
        self.comboBox_for_select_topic.setFont(font)
        self.comboBox_for_select_topic.setStyleSheet(u"color: white;\n"
"")
        self.label_for_connect_result = QLabel(self.centralwidget)
        self.label_for_connect_result.setObjectName(u"label_for_connect_result")
        self.label_for_connect_result.setGeometry(QRect(12, 270, 391, 21))
        self.label_for_connect_result.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 20, 261, 16))
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"  color: white;\n"
"  font-family: 'Montserrat', sans-serif;\n"
"  font-size: 11px;\n"
"  text-transform: uppercase;\n"
"  text-align: center;\n"
"  letter-spacing: 3px;\n"
"  font-weight: 600;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit_for_view.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Montserrat'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_for_sendmessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_for_connect_result.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u043e\u0440 \u0442\u043e\u043f\u0438\u043a\u0430 \u0434\u043b\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438</p></body></html>", None))
    # retranslateUi

