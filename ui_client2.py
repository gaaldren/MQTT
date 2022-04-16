# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client2ODfzAy.ui'
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
        MainWindow.resize(858, 459)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: #37393d")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 861, 31))
        font = QFont()
        font.setFamily(u"Montserrat Black")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(57, 64, 72);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_ghost_w = QPushButton(self.frame)
        self.pushButton_ghost_w.setObjectName(u"pushButton_ghost_w")
        self.pushButton_ghost_w.setGeometry(QRect(730, 0, 61, 31))
        self.pushButton_ghost_w.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(56, 92, 255);\n"
"}")
        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(800, 0, 61, 31))
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 17, 0);\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 0, 61, 31))
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 29, 131, 431))
        self.frame_3.setStyleSheet(u"background-color: rgb(57, 64, 72);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_page1 = QPushButton(self.frame_3)
        self.pushButton_page1.setObjectName(u"pushButton_page1")
        self.pushButton_page1.setGeometry(QRect(0, 0, 131, 51))
        font2 = QFont()
        font2.setFamily(u"Montserrat Medium")
        font2.setPointSize(12)
        font2.setItalic(False)
        self.pushButton_page1.setFont(font2)
        self.pushButton_page1.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(56, 92, 255);\n"
"}")
        self.pushButton_page2 = QPushButton(self.frame_3)
        self.pushButton_page2.setObjectName(u"pushButton_page2")
        self.pushButton_page2.setGeometry(QRect(0, 50, 131, 51))
        self.pushButton_page2.setFont(font2)
        self.pushButton_page2.setStyleSheet(u"QPushButton {\n"
" color: rgb(255, 255, 255);\n"
"background-color: rgb(57, 64, 72);\n"
" border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(56, 92, 255);\n"
"}")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(5, 400, 61, 31))
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(139, 39, 721, 411))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.btn_for_sendmessage2 = QPushButton(self.page)
        self.btn_for_sendmessage2.setObjectName(u"btn_for_sendmessage2")
        self.btn_for_sendmessage2.setGeometry(QRect(460, 369, 201, 41))
        font4 = QFont()
        font4.setFamily(u"Montserrat Medium")
        font4.setPointSize(11)
        font4.setItalic(False)
        self.btn_for_sendmessage2.setFont(font4)
        self.btn_for_sendmessage2.setStyleSheet(u"background-color: rgb(56, 92, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.textEdit_for_view2 = QTextEdit(self.page)
        self.textEdit_for_view2.setObjectName(u"textEdit_for_view2")
        self.textEdit_for_view2.setGeometry(QRect(0, 4, 404, 341))
        self.textEdit_for_view2.setFont(font2)
        self.textEdit_for_view2.setStyleSheet(u"background-color: #37393d;\n"
" color: white;\n"
"border-radius: 1px solid;\n"
"border-color: #37393d;\n"
"")
        self.comboBox_for_select_topic2 = QComboBox(self.page)
        self.comboBox_for_select_topic2.setObjectName(u"comboBox_for_select_topic2")
        self.comboBox_for_select_topic2.setGeometry(QRect(430, 4, 260, 40))
        font5 = QFont()
        font5.setFamily(u"Montserrat Medium")
        font5.setPointSize(10)
        font5.setItalic(False)
        self.comboBox_for_select_topic2.setFont(font5)
        self.comboBox_for_select_topic2.setStyleSheet(u"QComboBox{\n"
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
"selection-background-color:  rgb(56, 92, 255);\n"
"}\n"
"")
        self.lineEdit_for_writetext2 = QLineEdit(self.page)
        self.lineEdit_for_writetext2.setObjectName(u"lineEdit_for_writetext2")
        self.lineEdit_for_writetext2.setGeometry(QRect(0, 370, 404, 40))
        font6 = QFont()
        font6.setFamily(u"Montserrat Medium")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setWeight(50)
        font6.setStrikeOut(False)
        self.lineEdit_for_writetext2.setFont(font6)
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
        self.textEdit.setGeometry(QRect(3, 10, 701, 391))
        font7 = QFont()
        font7.setFamily(u"Montserrat Medium")
        self.textEdit.setFont(font7)
        self.textEdit.setStyleSheet(u"border-width: 0px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_ghost_w.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">MQQT</span></p></body></html>", None))
        self.pushButton_page1.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_page2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043b\u0438\u0435\u043d\u0442 2</p></body></html>", None))
        self.btn_for_sendmessage2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.textEdit_for_view2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Montserrat Medium'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Montserrat'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.lineEdit_for_writetext2.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Montserrat Medium'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">1. mqtt/text/chat \u2014 \u0442\u043e\u043f\u0438\u043a, \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">2. device"
                        "/memorystatus/harddrive/c \u2014 \u0442\u043e\u043f\u0438\u043a, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0434\u0438\u0441\u043a\u0430 &quot;C&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">3. device/work/cpu \u2014 \u0442\u043e\u043f\u0438\u043a, \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0440\u0430\u0431\u043e\u0442\u0443 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430 \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">4. device/work/ram \u2014 \u0442\u043e\u043f\u0438\u043a, \u043f\u043e\u043a\u0430\u0437\u044b\u0432"
                        "\u0430\u044e\u0449\u0438\u0439 \u0440\u0430\u0431\u043e\u0442\u0443 \u043f\u0430\u043c\u044f\u0442\u0438 \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">5. music/track1/start \u2014 \u0442\u043e\u043f\u0438\u043a \u043d\u0430 \u0437\u0430\u043f\u0443\u0441\u043a \u0442\u0440\u0435\u043a\u0430. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">6. music/track1/stop \u2014 \u0442\u043e\u043f\u0438\u043a \u043d\u0430 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443 \u0442\u0440\u0435\u043a\u0430. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-family:'MS Shell Dlg 2'; font-size:12pt;\">7. android/get_ascll \u2014 \u0442\u043e\u043f\u0438\u043a \u043d\u0430 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u0433\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">8. android/get_ip/return \u2014 \u0442\u043e\u043f\u0438\u043a \u043d\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 ip \u0430\u0434\u0440\u0435\u0441\u0430 \u0430\u043d\u0434\u0440\u043e\u0438\u0434\u0430. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">9. android/tts \u2014 \u0442\u043e\u043f\u0438\u043a, \u043e\u0442\u0432\u0435\u0447\u0430\u044e"
                        "\u0449\u0438\u0439 \u0437\u0430 \u0432\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432 \u0440\u0435\u0447\u044c.</span></p></body></html>", None))
    # retranslateUi

