# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client2TkeRkT.ui'
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
        MainWindow.resize(860, 460)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: #37393d")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 861, 51))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_ghost_w = QPushButton(self.frame)
        self.pushButton_ghost_w.setObjectName(u"pushButton_ghost_w")
        self.pushButton_ghost_w.setGeometry(QRect(730, 0, 61, 51))
        self.pushButton_ghost_w.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: black;\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(55,55,55);\n"
"}")
        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(800, 0, 61, 51))
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: black;\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 17, 0);\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 81, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 10, 51, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-1, 49, 131, 411))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_page1 = QPushButton(self.frame_3)
        self.pushButton_page1.setObjectName(u"pushButton_page1")
        self.pushButton_page1.setGeometry(QRect(0, 0, 131, 51))
        font = QFont()
        font.setPointSize(12)
        self.pushButton_page1.setFont(font)
        self.pushButton_page1.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: black;\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(55,55,55);\n"
"}")
        self.pushButton_page2 = QPushButton(self.frame_3)
        self.pushButton_page2.setObjectName(u"pushButton_page2")
        self.pushButton_page2.setGeometry(QRect(0, 50, 131, 51))
        self.pushButton_page2.setFont(font)
        self.pushButton_page2.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: black;\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(55,55,55);\n"
"}")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(139, 59, 721, 391))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.btn_for_sendmessage2 = QPushButton(self.page)
        self.btn_for_sendmessage2.setObjectName(u"btn_for_sendmessage2")
        self.btn_for_sendmessage2.setGeometry(QRect(430, 312, 260, 40))
        self.btn_for_sendmessage2.setStyleSheet(u"background-color: rgb(114, 255, 112);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.textEdit_for_view2 = QTextEdit(self.page)
        self.textEdit_for_view2.setObjectName(u"textEdit_for_view2")
        self.textEdit_for_view2.setGeometry(QRect(0, 4, 404, 302))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.textEdit_for_view2.setFont(font1)
        self.textEdit_for_view2.setStyleSheet(u"background-color: #37393d;\n"
" color: white;\n"
"border-radius: 1px solid;\n"
"border-color: #37393d;\n"
"")
        self.comboBox_for_select_topic2 = QComboBox(self.page)
        self.comboBox_for_select_topic2.setObjectName(u"comboBox_for_select_topic2")
        self.comboBox_for_select_topic2.setGeometry(QRect(430, 4, 260, 40))
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        self.comboBox_for_select_topic2.setFont(font2)
        self.comboBox_for_select_topic2.setStyleSheet(u"background-color: rgb(76, 79, 84);\n"
"color: white;\n"
"\n"
"")
        self.lineEdit_for_writetext2 = QLineEdit(self.page)
        self.lineEdit_for_writetext2.setObjectName(u"lineEdit_for_writetext2")
        self.lineEdit_for_writetext2.setGeometry(QRect(0, 312, 404, 40))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.lineEdit_for_writetext2.setFont(font3)
        self.lineEdit_for_writetext2.setStyleSheet(u"background-color: #37393d;\n"
" color: white;\n"
"border-radius: 1px solid;\n"
"border-color: #37393d;\n"
"")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(3, 10, 701, 371))
        self.textEdit.setStyleSheet(u"border-width: 0px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_ghost_w.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">MQQT</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043b\u0438\u0435\u043d\u0442 2</p></body></html>", None))
        self.pushButton_page1.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_page2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.btn_for_sendmessage2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.textEdit_for_view2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Montserrat'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.lineEdit_for_writetext2.setText("")
    # retranslateUi

