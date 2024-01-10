# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logonAZKzRt.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import client.src.res.res_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(931, 601)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblCopyrightHolder = QLabel(self.centralwidget)
        self.lblCopyrightHolder.setObjectName(u"lblCopyrightHolder")
        self.lblCopyrightHolder.setGeometry(QRect(737, 570, 181, 20))
        self.fmLogon = QFrame(self.centralwidget)
        self.fmLogon.setObjectName(u"fmLogon")
        self.fmLogon.setGeometry(QRect(10, 10, 381, 581))
        self.fmLogon.setFrameShape(QFrame.StyledPanel)
        self.fmLogon.setFrameShadow(QFrame.Plain)
        self.lblBackground = QLabel(self.fmLogon)
        self.lblBackground.setObjectName(u"lblBackground")
        self.lblBackground.setGeometry(QRect(0, 0, 381, 581))
        self.lblBackground.setPixmap(QPixmap(u":/images/images/login-background-img.png"))
        self.lblBackground.setAlignment(Qt.AlignCenter)
        self.lblVersion_2 = QLabel(self.fmLogon)
        self.lblVersion_2.setObjectName(u"lblVersion_2")
        self.lblVersion_2.setGeometry(QRect(10, 560, 51, 16))
        self.lblVersion_2.setStyleSheet(u"QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.lblAppName = QLabel(self.fmLogon)
        self.lblAppName.setObjectName(u"lblAppName")
        self.lblAppName.setGeometry(QRect(110, 240, 131, 20))
        self.lblAppName.setStyleSheet(u"QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.lblAppName.setAlignment(Qt.AlignCenter)
        self.lblAppVersion = QLabel(self.fmLogon)
        self.lblAppVersion.setObjectName(u"lblAppVersion")
        self.lblAppVersion.setGeometry(QRect(60, 560, 91, 16))
        self.lblAppVersion.setStyleSheet(u"QLabel {\n"
"   color: rgb(220, 220, 220)\n"
"}\n"
"")
        self.lblDes1 = QLabel(self.fmLogon)
        self.lblDes1.setObjectName(u"lblDes1")
        self.lblDes1.setGeometry(QRect(130, 320, 91, 16))
        self.lblDes1.setStyleSheet(u"QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.lblDes1.setAlignment(Qt.AlignCenter)
        self.lblDes2 = QLabel(self.fmLogon)
        self.lblDes2.setObjectName(u"lblDes2")
        self.lblDes2.setGeometry(QRect(130, 340, 91, 16))
        self.lblDes2.setStyleSheet(u"QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.lblDes2.setAlignment(Qt.AlignCenter)
        self.lblDes3 = QLabel(self.fmLogon)
        self.lblDes3.setObjectName(u"lblDes3")
        self.lblDes3.setGeometry(QRect(130, 360, 91, 16))
        self.lblDes3.setStyleSheet(u"QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.lblDes3.setAlignment(Qt.AlignCenter)
        self.lblAppIcon = QLabel(self.fmLogon)
        self.lblAppIcon.setObjectName(u"lblAppIcon")
        self.lblAppIcon.setGeometry(QRect(130, 150, 91, 81))
        self.lblAppIcon.setAutoFillBackground(False)
        self.lblAppIcon.setPixmap(QPixmap(u":/icons/icons/random-client-icon.png"))
        self.lblAppIcon.setScaledContents(True)
        self.lblAppDes = QLabel(self.fmLogon)
        self.lblAppDes.setObjectName(u"lblAppDes")
        self.lblAppDes.setGeometry(QRect(60, 260, 231, 20))
        self.lblAppDes.setStyleSheet(u"QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.lblAppDes.setAlignment(Qt.AlignCenter)
        self.fmLogonInfo = QFrame(self.centralwidget)
        self.fmLogonInfo.setObjectName(u"fmLogonInfo")
        self.fmLogonInfo.setGeometry(QRect(460, 110, 331, 381))
        self.fmLogonInfo.setFrameShape(QFrame.StyledPanel)
        self.fmLogonInfo.setFrameShadow(QFrame.Raised)
        self.lePasswd = QLineEdit(self.fmLogonInfo)
        self.lePasswd.setObjectName(u"lePasswd")
        self.lePasswd.setGeometry(QRect(80, 220, 211, 31))
        self.lePasswd.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 0;\n"
"	border: 1px solid rgb(159, 159, 159),\n"
"\n"
"}\n"
"")
        self.lePasswd.setEchoMode(QLineEdit.Password)
        self.lePasswd.setAlignment(Qt.AlignCenter)
        self.lblUserIcon = QLabel(self.fmLogonInfo)
        self.lblUserIcon.setObjectName(u"lblUserIcon")
        self.lblUserIcon.setGeometry(QRect(50, 140, 31, 31))
        self.lblUserIcon.setAutoFillBackground(False)
        self.lblUserIcon.setPixmap(QPixmap(u":/icons/icons/contacts-icon.png"))
        self.lblUserIcon.setScaledContents(True)
        self.lblLogInto = QLabel(self.fmLogonInfo)
        self.lblLogInto.setObjectName(u"lblLogInto")
        self.lblLogInto.setGeometry(QRect(50, 50, 191, 16))
        self.leUsername = QLineEdit(self.fmLogonInfo)
        self.leUsername.setObjectName(u"leUsername")
        self.leUsername.setGeometry(QRect(80, 140, 211, 31))
        self.leUsername.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding: 5px 0;\n"
"	border: 1px solid rgb(159, 159, 159),\n"
"\n"
"}\n"
"")
        self.leUsername.setMaxLength(30)
        self.leUsername.setAlignment(Qt.AlignCenter)
        self.btnClear = QPushButton(self.fmLogonInfo)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(50, 310, 111, 41))
        self.lblForgotPasswordLink = QLabel(self.fmLogonInfo)
        self.lblForgotPasswordLink.setObjectName(u"lblForgotPasswordLink")
        self.lblForgotPasswordLink.setGeometry(QRect(150, 200, 141, 16))
        self.lblForgotPasswordLink.setStyleSheet(u"QLabel:hover {\n"
"    color: #FF0000; /* Red */\n"
"}")
        self.lblInstructions = QLabel(self.fmLogonInfo)
        self.lblInstructions.setObjectName(u"lblInstructions")
        self.lblInstructions.setGeometry(QRect(50, 70, 241, 16))
        self.lblPasswd = QLabel(self.fmLogonInfo)
        self.lblPasswd.setObjectName(u"lblPasswd")
        self.lblPasswd.setGeometry(QRect(50, 200, 61, 16))
        self.btnRememberMe = QCheckBox(self.fmLogonInfo)
        self.btnRememberMe.setObjectName(u"btnRememberMe")
        self.btnRememberMe.setGeometry(QRect(50, 270, 111, 20))
        self.btnSignIn = QPushButton(self.fmLogonInfo)
        self.btnSignIn.setObjectName(u"btnSignIn")
        self.btnSignIn.setGeometry(QRect(179, 310, 111, 41))
        self.lblUsername = QLabel(self.fmLogonInfo)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(50, 120, 241, 16))
        self.lblPassIncon = QLabel(self.fmLogonInfo)
        self.lblPassIncon.setObjectName(u"lblPassIncon")
        self.lblPassIncon.setGeometry(QRect(50, 220, 31, 31))
        self.lblPassIncon.setAutoFillBackground(False)
        self.lblPassIncon.setPixmap(QPixmap(u":/icons/icons/key-icon.png"))
        self.lblPassIncon.setScaledContents(True)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.lblCopyrightHolder.setText(QCoreApplication.translate("LoginWindow", u"[Copyright information holder]", None))
        self.lblBackground.setText("")
        self.lblVersion_2.setText(QCoreApplication.translate("LoginWindow", u"Version:", None))
        self.lblAppName.setText(QCoreApplication.translate("LoginWindow", u"[Application Name]", None))
        self.lblAppVersion.setText(QCoreApplication.translate("LoginWindow", u"[APP Version]", None))
        self.lblDes1.setText(QCoreApplication.translate("LoginWindow", u"[Description 1]", None))
        self.lblDes2.setText(QCoreApplication.translate("LoginWindow", u"[Description 1]", None))
        self.lblDes3.setText(QCoreApplication.translate("LoginWindow", u"[Description 1]", None))
        self.lblAppIcon.setText("")
        self.lblAppDes.setText(QCoreApplication.translate("LoginWindow", u"[Application WORDS Description]", None))
        self.lePasswd.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.lblUserIcon.setText("")
        self.lblLogInto.setText(QCoreApplication.translate("LoginWindow", u"Log Into [APPLICATION NAME]", None))
        self.leUsername.setInputMask("")
        self.leUsername.setText("")
        self.leUsername.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.btnClear.setText(QCoreApplication.translate("LoginWindow", u"Clear", None))
        self.lblForgotPasswordLink.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"right\">[Forgot Password Link]</p></body></html>", None))
        self.lblInstructions.setText(QCoreApplication.translate("LoginWindow", u"Enter your Username and Password", None))
        self.lblPasswd.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.btnRememberMe.setText(QCoreApplication.translate("LoginWindow", u"Remember Me", None))
        self.btnSignIn.setText(QCoreApplication.translate("LoginWindow", u"Sign In", None))
        self.lblUsername.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.lblPassIncon.setText("")
    # retranslateUi

