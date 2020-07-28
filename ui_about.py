# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(400, 287)
        About.setStyleSheet(u"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #353535;\n"
"}\n"
"QCheckBox:disabled {\n"
"color: grey;\n"
"}\n"
"#head_model, #hair_model, #top_model, #bottom_model {\n"
"border: 1px solid #121212;\n"
"border-radius: 3px;\n"
"}\n"
"#head_model:on, #hair_model:on, #top_model:on, #bottom_model:on, #head_model:focus, #hair_model:focus, #top_model:focus, #bottom_model:focus {border: 1px solid #53a0ed;}\n"
"\n"
"#pick_game::item:selected, #pick_new_game::item:selected {\n"
"background-color: #388bdd;\n"
"border: none;\n"
"color: black;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"color: black;\n"
"background-color:  #388bdd;\n"
"}\n"
"QMenuBar::item:selected {\n"
"color: black;\n"
"background-color: #3884cd ;\n"
"}\n"
"#head_model {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"#hair_model {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"#top_model {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"#bottom_model {\n"
"background-color: #121212;\n"
""
                        "color: #CCCCCC;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"QListWidget {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"QLabel {\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"QCheckBox {\n"
"background-color: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: #454545;\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"     background: #454545;\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: #454545;\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"     background: #454545;\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontr"
                        "ol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: black;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: #222222;\n"
"      width: 15px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: #454545;\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"     background: #454545;\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"    background: #45"
                        "4545;\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: black;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}")
        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 21, 141, 41))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.textBrowser = QTextBrowser(About)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(25, 71, 341, 161))
        self.textBrowser.setOpenExternalLinks(True)
        self.pushButton = QPushButton(About)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 250, 75, 23))

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.label.setText(QCoreApplication.translate("About", u"dmdEditor", None))
        self.textBrowser.setHtml(QCoreApplication.translate("About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tool for editing character_model_model_data.bin</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />Made by Timo654.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to MnSXx, Capitan Retraso and etra0 for helping.</p>\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to MikoM, Kent, ketruB, Foas and jason098 for testing.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Come join us at the Yakuza Modding Community discord server</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://discord.com/invite/WsV9XVE\"><span style=\" font-size:8pt; text-decoration: underline; color:#8fa0ff;\">https://discord.com/invite/WsV9XVE</span></a></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("About", u"OK", None))
    # retranslateUi

