# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'publisherbFDRyE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_pub_form(object):
    def setupUi(self, pub_form):
        if not pub_form.objectName():
            pub_form.setObjectName(u"pub_form")
        pub_form.resize(457, 272)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setItalic(False)
        pub_form.setFont(font)
        pub_form.setLayoutDirection(Qt.LeftToRight)
        self.pub_message_lable = QLabel(pub_form)
        self.pub_message_lable.setObjectName(u"pub_message_lable")
        self.pub_message_lable.setGeometry(QRect(30, 20, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code SemiLight")
        font1.setPointSize(12)
        font1.setItalic(False)
        self.pub_message_lable.setFont(font1)
        self.pub_send_button = QPushButton(pub_form)
        self.pub_send_button.setObjectName(u"pub_send_button")
        self.pub_send_button.setGeometry(QRect(330, 220, 101, 31))
        self.pub_send_button.setFont(font1)
        self.pub_message_box = QTextEdit(pub_form)
        self.pub_message_box.setObjectName(u"pub_message_box")
        self.pub_message_box.setGeometry(QRect(30, 50, 401, 161))
        self.pub_message_box.setFont(font1)

        self.retranslateUi(pub_form)

        QMetaObject.connectSlotsByName(pub_form)
    # setupUi

    def retranslateUi(self, pub_form):
        pub_form.setWindowTitle(QCoreApplication.translate("pub_form", u"\u0418\u0437\u0434\u0430\u0442\u0435\u043b\u044c", None))
        self.pub_message_lable.setText(QCoreApplication.translate("pub_form", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.pub_send_button.setText(QCoreApplication.translate("pub_form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

