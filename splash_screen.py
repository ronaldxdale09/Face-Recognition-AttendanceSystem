# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashUXiOkm.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import splash_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 401)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	background-color:rgb(53, 53, 53);\n"
"	color:rgb(220, 220, 220);\n"
"	border-radius:15px;\n"
"\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 140, 661, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color:rgb(255, 137, 139)")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_wmsu = QLabel(self.dropShadowFrame)
        self.label_wmsu.setObjectName(u"label_wmsu")
        self.label_wmsu.setGeometry(QRect(0, 130, 661, 21))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_wmsu.setFont(font1)
        self.label_wmsu.setStyleSheet(u"color:rgb(255, 137, 139)")
        self.label_wmsu.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 260, 521, 31))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(122, 122, 122);\n"
"	color:rgb(200,200,200);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color:rgb(255, 137, 139)	\n"
"}")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 10, 101, 101))
        self.label_3.setMinimumSize(QSize(101, 81))
        self.label_3.setMaximumSize(QSize(301, 281))
        self.label_3.setPixmap(QPixmap(u":/logo/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.dropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 290, 661, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:rgb(255, 137, 139)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(320, 350, 451, 31))
        font2 = QFont()
        font2.setPointSize(7)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color:rgb(255, 137, 139)")
        self.label_credits.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<strong> FACE RECOGNITION </strong> SYSTEM", None))
        self.label_wmsu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>WESTERN MINDANAO STATE UNIVERSITY</p></body></html>", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>loading...</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Created</span>: Ronald Dale Fuentebella &amp; Joshua Habil</p></body></html>", None))
    # retranslateUi

