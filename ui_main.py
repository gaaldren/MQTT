# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFmcyjO.ui'
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
        MainWindow.resize(383, 166)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(106, 30, 171, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.sub_button = QPushButton(self.centralwidget)
        self.sub_button.setObjectName(u"sub_button")
        self.sub_button.setGeometry(QRect(20, 90, 121, 41))
        self.sub_button.setFont(font)
        self.pub_button = QPushButton(self.centralwidget)
        self.pub_button.setObjectName(u"pub_button")
        self.pub_button.setGeometry(QRect(230, 90, 121, 41))
        self.pub_button.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u043e\u0440 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</p></body></html>", None))
        self.sub_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a", None))
        self.pub_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0434\u0442\u0430\u0442\u0435\u043b\u044c", None))
    # retranslateUi

