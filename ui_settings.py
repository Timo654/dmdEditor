# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(601, 655)
        Settings.setStyleSheet(u"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #353535;\n"
"}\n"
"QCheckBox:disabled {\n"
"color: grey;\n"
"}\n"
"\n"
"QCheckBox:enabled {\n"
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
"      border: "
                        "1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"     background: #454545;\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
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
"      subcontrol-or"
                        "igin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"    background: #454545;\n"
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
        self.lexus2_label = QLabel(Settings)
        self.lexus2_label.setObjectName(u"lexus2_label")
        self.lexus2_label.setGeometry(QRect(50, 60, 201, 20))
        self.lexus2_parts_label = QLabel(Settings)
        self.lexus2_parts_label.setObjectName(u"lexus2_parts_label")
        self.lexus2_parts_label.setGeometry(QRect(50, 120, 201, 20))
        self.ogref_label = QLabel(Settings)
        self.ogref_label.setObjectName(u"ogref_label")
        self.ogref_label.setGeometry(QRect(50, 180, 201, 20))
        self.ogref_parts_label = QLabel(Settings)
        self.ogref_parts_label.setObjectName(u"ogref_parts_label")
        self.ogref_parts_label.setGeometry(QRect(50, 240, 201, 20))
        self.settings_label = QLabel(Settings)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setGeometry(QRect(40, 20, 151, 31))
        font = QFont()
        font.setPointSize(12)
        self.settings_label.setFont(font)
        self.frame = QFrame(Settings)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 541, 531))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(7, 220, 521, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 160, 521, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 100, 521, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 40, 521, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(10, 280, 521, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 340, 521, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 400, 521, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(10, 460, 521, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.table_lexus2 = QLineEdit(Settings)
        self.table_lexus2.setObjectName(u"table_lexus2")
        self.table_lexus2.setGeometry(QRect(50, 80, 371, 23))
        self.table_lexus2_parts = QLineEdit(Settings)
        self.table_lexus2_parts.setObjectName(u"table_lexus2_parts")
        self.table_lexus2_parts.setGeometry(QRect(50, 140, 371, 23))
        self.table_ogref = QLineEdit(Settings)
        self.table_ogref.setObjectName(u"table_ogref")
        self.table_ogref.setGeometry(QRect(50, 200, 371, 23))
        self.table_ogref_parts = QLineEdit(Settings)
        self.table_ogref_parts.setObjectName(u"table_ogref_parts")
        self.table_ogref_parts.setGeometry(QRect(50, 260, 371, 23))
        self.select_lexus2 = QPushButton(Settings)
        self.select_lexus2.setObjectName(u"select_lexus2")
        self.select_lexus2.setGeometry(QRect(450, 80, 91, 23))
        self.select_ogref = QPushButton(Settings)
        self.select_ogref.setObjectName(u"select_ogref")
        self.select_ogref.setGeometry(QRect(450, 200, 91, 23))
        self.select_ogref_parts = QPushButton(Settings)
        self.select_ogref_parts.setObjectName(u"select_ogref_parts")
        self.select_ogref_parts.setGeometry(QRect(450, 260, 91, 23))
        self.select_lexus2_parts = QPushButton(Settings)
        self.select_lexus2_parts.setObjectName(u"select_lexus2_parts")
        self.select_lexus2_parts.setGeometry(QRect(450, 140, 91, 23))
        self.persona_label = QLabel(Settings)
        self.persona_label.setObjectName(u"persona_label")
        self.persona_label.setGeometry(QRect(50, 300, 201, 20))
        self.table_persona = QLineEdit(Settings)
        self.table_persona.setObjectName(u"table_persona")
        self.table_persona.setGeometry(QRect(50, 320, 371, 23))
        self.judge_label = QLabel(Settings)
        self.judge_label.setObjectName(u"judge_label")
        self.judge_label.setGeometry(QRect(50, 420, 201, 20))
        self.table_judge_parts = QLineEdit(Settings)
        self.table_judge_parts.setObjectName(u"table_judge_parts")
        self.table_judge_parts.setGeometry(QRect(50, 500, 371, 23))
        self.table_persona_parts = QLineEdit(Settings)
        self.table_persona_parts.setObjectName(u"table_persona_parts")
        self.table_persona_parts.setGeometry(QRect(50, 380, 371, 23))
        self.table_judge = QLineEdit(Settings)
        self.table_judge.setObjectName(u"table_judge")
        self.table_judge.setGeometry(QRect(50, 440, 371, 23))
        self.judge_parts_label = QLabel(Settings)
        self.judge_parts_label.setObjectName(u"judge_parts_label")
        self.judge_parts_label.setGeometry(QRect(50, 480, 201, 20))
        self.persona_parts_label = QLabel(Settings)
        self.persona_parts_label.setObjectName(u"persona_parts_label")
        self.persona_parts_label.setGeometry(QRect(50, 360, 201, 20))
        self.select_persona = QPushButton(Settings)
        self.select_persona.setObjectName(u"select_persona")
        self.select_persona.setGeometry(QRect(450, 320, 91, 23))
        self.select_persona_parts = QPushButton(Settings)
        self.select_persona_parts.setObjectName(u"select_persona_parts")
        self.select_persona_parts.setGeometry(QRect(450, 380, 91, 23))
        self.select_judge = QPushButton(Settings)
        self.select_judge.setObjectName(u"select_judge")
        self.select_judge.setGeometry(QRect(450, 440, 91, 23))
        self.select_judge_parts = QPushButton(Settings)
        self.select_judge_parts.setObjectName(u"select_judge_parts")
        self.select_judge_parts.setGeometry(QRect(450, 500, 91, 23))
        self.cancel_button_s = QPushButton(Settings)
        self.cancel_button_s.setObjectName(u"cancel_button_s")
        self.cancel_button_s.setGeometry(QRect(430, 560, 68, 23))
        self.save_button_s = QPushButton(Settings)
        self.save_button_s.setObjectName(u"save_button_s")
        self.save_button_s.setGeometry(QRect(504, 560, 68, 23))
        self.default_button = QPushButton(Settings)
        self.default_button.setObjectName(u"default_button")
        self.default_button.setGeometry(QRect(333, 560, 91, 23))
        self.frame.raise_()
        self.lexus2_label.raise_()
        self.lexus2_parts_label.raise_()
        self.ogref_label.raise_()
        self.ogref_parts_label.raise_()
        self.settings_label.raise_()
        self.table_lexus2.raise_()
        self.table_lexus2_parts.raise_()
        self.table_ogref.raise_()
        self.table_ogref_parts.raise_()
        self.select_lexus2.raise_()
        self.select_ogref.raise_()
        self.select_ogref_parts.raise_()
        self.select_lexus2_parts.raise_()
        self.persona_label.raise_()
        self.table_persona.raise_()
        self.judge_label.raise_()
        self.table_judge_parts.raise_()
        self.table_persona_parts.raise_()
        self.table_judge.raise_()
        self.judge_parts_label.raise_()
        self.persona_parts_label.raise_()
        self.select_persona.raise_()
        self.select_persona_parts.raise_()
        self.select_judge.raise_()
        self.select_judge_parts.raise_()
        self.cancel_button_s.raise_()
        self.save_button_s.raise_()
        self.default_button.raise_()

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.lexus2_label.setText(QCoreApplication.translate("Settings", u"Yakuza Kiwami 2 model_data table", None))
        self.lexus2_parts_label.setText(QCoreApplication.translate("Settings", u"Yakuza Kiwami 2 model parts table", None))
        self.ogref_label.setText(QCoreApplication.translate("Settings", u"Yakuza 6 model_data table", None))
        self.ogref_parts_label.setText(QCoreApplication.translate("Settings", u"Yakuza 6 model parts table", None))
        self.settings_label.setText(QCoreApplication.translate("Settings", u"Settings", None))
        self.select_lexus2.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.select_ogref.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.select_ogref_parts.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.select_lexus2_parts.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.persona_label.setText(QCoreApplication.translate("Settings", u"Yakuza Like a Dragon model_data table", None))
        self.judge_label.setText(QCoreApplication.translate("Settings", u"Judgment model_data table", None))
        self.judge_parts_label.setText(QCoreApplication.translate("Settings", u"Judgment model parts table", None))
        self.persona_parts_label.setText(QCoreApplication.translate("Settings", u"Yakuza Like a Dragon model parts table", None))
        self.select_persona.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.select_persona_parts.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.select_judge.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.select_judge_parts.setText(QCoreApplication.translate("Settings", u"Select a file", None))
        self.cancel_button_s.setText(QCoreApplication.translate("Settings", u"Cancel", None))
        self.save_button_s.setText(QCoreApplication.translate("Settings", u"Save", None))
        self.default_button.setText(QCoreApplication.translate("Settings", u"Reset to default", None))
    # retranslateUi

