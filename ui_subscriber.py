# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subscriberrUnUJl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sub_form(object):
    def setupUi(self, sub_form):
        if not sub_form.objectName():
            sub_form.setObjectName(u"sub_form")
        sub_form.resize(457, 272)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setItalic(False)
        sub_form.setFont(font)
        sub_form.setLayoutDirection(Qt.LeftToRight)
        sub_form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sub_message_lable = QLabel(sub_form)
        self.sub_message_lable.setObjectName(u"sub_message_lable")
        self.sub_message_lable.setGeometry(QRect(30, 20, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code SemiLight")
        font1.setPointSize(12)
        font1.setItalic(False)
        self.sub_message_lable.setFont(font1)
        self.label_for_connect_result = QLabel(sub_form)
        self.label_for_connect_result.setObjectName(u"label_for_connect_result")
        self.label_for_connect_result.setGeometry(QRect(40, 230, 271, 16))
        self.textEdit = QTextEdit(sub_form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 50, 411, 161))

        self.retranslateUi(sub_form)

        QMetaObject.connectSlotsByName(sub_form)
    # setupUi

    def retranslateUi(self, sub_form):
        sub_form.setWindowTitle(QCoreApplication.translate("sub_form", u"\u041f\u043e\u0434\u043f\u0438\u0441\u0447\u0438\u043a", None))
        self.sub_message_lable.setText(QCoreApplication.translate("sub_form", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.label_for_connect_result.setText("")
    # retranslateUi

