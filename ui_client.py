# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientUBRRlv.ui'
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
        MainWindow.setMinimumSize(QSize(860, 460))
        MainWindow.setMaximumSize(QSize(860, 460))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: #37393d")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 861, 31))
        self.frame.setStyleSheet(u"background-color: rgb(57, 64, 72);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(800, 0, 61, 31))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 17, 0);\n"
"}")
        self.btn_ghost = QPushButton(self.frame)
        self.btn_ghost.setObjectName(u"btn_ghost")
        self.btn_ghost.setGeometry(QRect(730, 0, 61, 31))
        self.btn_ghost.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(83, 0, 191);\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 61, 31))
        font = QFont()
        font.setFamily(u"Montserrat Medium")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 29, 131, 431))
        self.frame_2.setStyleSheet(u"background-color: rgb(57, 64, 72);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_page1 = QPushButton(self.frame_2)
        self.pushButton_page1.setObjectName(u"pushButton_page1")
        self.pushButton_page1.setGeometry(QRect(0, 0, 131, 51))
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setPointSize(12)
        self.pushButton_page1.setFont(font1)
        self.pushButton_page1.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(83, 0, 191);\n"
"}")
        self.pushButton_page2 = QPushButton(self.frame_2)
        self.pushButton_page2.setObjectName(u"pushButton_page2")
        self.pushButton_page2.setGeometry(QRect(0, 50, 131, 51))
        self.pushButton_page2.setFont(font1)
        self.pushButton_page2.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(83, 0, 191);\n"
"}")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(5, 400, 51, 31))
        font2 = QFont()
        font2.setFamily(u"Montserrat Medium")
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(139, 39, 721, 411))
        self.stackedWidget.setStyleSheet(u"background-color: #37393d")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.btn_for_sendmessage = QPushButton(self.page_1)
        self.btn_for_sendmessage.setObjectName(u"btn_for_sendmessage")
        self.btn_for_sendmessage.setGeometry(QRect(460, 369, 201, 41))
        self.btn_for_sendmessage.setMinimumSize(QSize(40, 40))
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(11)
        self.btn_for_sendmessage.setFont(font3)
        self.btn_for_sendmessage.setStyleSheet(u"background-color: rgb(83, 0, 191);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.textEdit_for_view = QTextEdit(self.page_1)
        self.textEdit_for_view.setObjectName(u"textEdit_for_view")
        self.textEdit_for_view.setGeometry(QRect(0, 4, 404, 341))
        self.textEdit_for_view.setFont(font1)
        self.textEdit_for_view.setStyleSheet(u"background-color: #37393d;\n"
" color: white;\n"
"border-radius: 1px solid;\n"
"border-color: #37393d;\n"
"")
        self.comboBox_for_select_topic = QComboBox(self.page_1)
        self.comboBox_for_select_topic.setObjectName(u"comboBox_for_select_topic")
        self.comboBox_for_select_topic.setGeometry(QRect(430, 4, 260, 40))
        self.comboBox_for_select_topic.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamily(u"Montserrat Medium")
        font4.setPointSize(10)
        self.comboBox_for_select_topic.setFont(font4)
        self.comboBox_for_select_topic.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(57, 64, 72);\n"
"color: white;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-top-right-radius: 10px; \n"
"     border-bottom-right-radius: 10px;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"border: 1px solid darkgray;\n"
"selection-background-color:  rgb(83, 0, 191);\n"
"}\n"
"")
        self.lineEdit_for_writetext = QLineEdit(self.page_1)
        self.lineEdit_for_writetext.setObjectName(u"lineEdit_for_writetext")
        self.lineEdit_for_writetext.setGeometry(QRect(0, 370, 404, 40))
        self.lineEdit_for_writetext.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamily(u"Montserrat Medium")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setUnderline(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        self.lineEdit_for_writetext.setFont(font5)
        self.lineEdit_for_writetext.setStyleSheet(u" background: #37393d;\n"
" color: white;\n"
"border-radius: 1px solid;")
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.textEdit = QTextEdit(self.page_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(3, 0, 701, 401))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"border-width: 0px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_ghost.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MQQT</span></p></body></html>", None))
        self.pushButton_page1.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_page2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043b\u0438\u0435\u043d\u0442 1 </p></body></html>", None))
        self.btn_for_sendmessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.textEdit_for_view.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Montserrat Medium'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Montserrat'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Montserrat Medium'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">1. mqtt/example1 \u2014 \u0442\u043e\u043f\u0438\u043a, \u043e\u0442\u0432\u0435\u0447\u0430\u044e\u0449\u0438\u0439 \u0437\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">2. device/ip \u2014 \u0442\u043e\u043f\u0438\u043a, \u043f\u043e"
                        "\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 ip \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">3. mqtt/picture \u2014 \u0442\u043e\u043f\u0438\u043a, \u0432\u044b\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">4. mqtt/get_weather/temp \u2014 \u0442\u043e\u043f\u0438\u043a, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0443 \u0432\u043e\u0437\u0434\u0443\u0445\u0430. </span></p>\n"
"<p "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">5. mqtt/get_weather/status \u2014 \u0442\u043e\u043f\u0438\u043a, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0433\u043e\u0434\u0435. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">6. android/vibro \u2014 \u0442\u043e\u043f\u0438\u043a \u043d\u0430 3-\u0445 \u0441\u0435\u043a\u0443\u043d\u0434\u043d\u0443\u044e \u0432\u0438\u0431\u0440\u0430\u0446\u0438\u044e.</span></p></body></html>", None))
    # retranslateUi

