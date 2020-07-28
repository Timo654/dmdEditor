# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'swap_values.ui'
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


class Ui_swap_values(object):
    def setupUi(self, swap_values):
        if not swap_values.objectName():
            swap_values.setObjectName(u"swap_values")
        swap_values.resize(964, 647)
        swap_values.setStyleSheet(u"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #353535;\n"
"}\n"
"QCheckBox:disabled {\n"
"color: grey;\n"
"}\n"
"#face_model, #hair_model, #tops_model, #btms_model {\n"
"border: 1px solid #121212;\n"
"border-radius: 3px;\n"
"}\n"
"#face_model:on, #hair_model:on, #tops_model:on, #btms_model:on, #face_model:focus, #hair_model:focus, #tops_model:focus, #btms_model:focus {border: 1px solid #53a0ed;}\n"
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
"#face_model {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"#hair_model {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"#tops_model {\n"
"background-color: #121212;\n"
"color: #CCCCCC;\n"
"}\n"
"\n"
"#btms_model {\n"
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
        self.actionSettings = QAction(swap_values)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(swap_values)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSwapFlags = QAction(swap_values)
        self.actionSwapFlags.setObjectName(u"actionSwapFlags")
        self.actionSwapFlags.setCheckable(True)
        self.actionSwapFlags.setChecked(True)
        self.actionSave = QAction(swap_values)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLoad_new_bin = QAction(swap_values)
        self.actionLoad_new_bin.setObjectName(u"actionLoad_new_bin")
        self.actionAbout_dmdEditor = QAction(swap_values)
        self.actionAbout_dmdEditor.setObjectName(u"actionAbout_dmdEditor")
        self.centralwidget = QWidget(swap_values)
        self.centralwidget.setObjectName(u"centralwidget")
        self.model_list_label = QLabel(self.centralwidget)
        self.model_list_label.setObjectName(u"model_list_label")
        self.model_list_label.setGeometry(QRect(30, 20, 71, 16))
        font = QFont()
        font.setPointSize(12)
        self.model_list_label.setFont(font)
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setEnabled(True)
        self.save_button.setGeometry(QRect(840, 560, 101, 41))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.save_button.setFont(font1)
        self.save_button.setAutoFillBackground(False)
        self.save_button.setCheckable(False)
        self.model_list = QListWidget(self.centralwidget)
        self.model_list.setObjectName(u"model_list")
        self.model_list.setGeometry(QRect(30, 80, 451, 436))
        self.model_list.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.revert_button = QPushButton(self.centralwidget)
        self.revert_button.setObjectName(u"revert_button")
        self.revert_button.setEnabled(True)
        self.revert_button.setGeometry(QRect(720, 560, 101, 41))
        self.revert_button.setFont(font1)
        self.revert_button.setAutoFillBackground(False)
        self.revert_button.setCheckable(False)
        self.log_box = QTextEdit(self.centralwidget)
        self.log_box.setObjectName(u"log_box")
        self.log_box.setGeometry(QRect(30, 515, 451, 23))
        self.log_box.setReadOnly(True)
        self.new_model_list = QListWidget(self.centralwidget)
        self.new_model_list.setObjectName(u"new_model_list")
        self.new_model_list.setGeometry(QRect(490, 80, 451, 321))
        self.new_model_list.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.new_model_list_label = QLabel(self.centralwidget)
        self.new_model_list_label.setObjectName(u"new_model_list_label")
        self.new_model_list_label.setGeometry(QRect(490, 20, 181, 16))
        self.new_model_list_label.setFont(font)
        self.replace_tops_flag = QCheckBox(self.centralwidget)
        self.replace_tops_flag.setObjectName(u"replace_tops_flag")
        self.replace_tops_flag.setGeometry(QRect(500, 450, 171, 31))
        self.replace_face_flag = QCheckBox(self.centralwidget)
        self.replace_face_flag.setObjectName(u"replace_face_flag")
        self.replace_face_flag.setGeometry(QRect(500, 410, 171, 31))
        self.replace_hair_flag = QCheckBox(self.centralwidget)
        self.replace_hair_flag.setObjectName(u"replace_hair_flag")
        self.replace_hair_flag.setGeometry(QRect(500, 430, 171, 31))
        self.replace_btms_flag = QCheckBox(self.centralwidget)
        self.replace_btms_flag.setObjectName(u"replace_btms_flag")
        self.replace_btms_flag.setGeometry(QRect(500, 470, 171, 31))
        self.replace_btms_part = QCheckBox(self.centralwidget)
        self.replace_btms_part.setObjectName(u"replace_btms_part")
        self.replace_btms_part.setEnabled(False)
        self.replace_btms_part.setGeometry(QRect(810, 470, 171, 31))
        self.replace_tops_part = QCheckBox(self.centralwidget)
        self.replace_tops_part.setObjectName(u"replace_tops_part")
        self.replace_tops_part.setEnabled(False)
        self.replace_tops_part.setGeometry(QRect(810, 450, 171, 31))
        self.replace_hair_part = QCheckBox(self.centralwidget)
        self.replace_hair_part.setObjectName(u"replace_hair_part")
        self.replace_hair_part.setEnabled(False)
        self.replace_hair_part.setGeometry(QRect(810, 430, 171, 31))
        self.replace_face_part = QCheckBox(self.centralwidget)
        self.replace_face_part.setObjectName(u"replace_face_part")
        self.replace_face_part.setEnabled(False)
        self.replace_face_part.setGeometry(QRect(810, 410, 171, 31))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(490, 409, 461, 141))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(215, 10, 20, 91))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.replace_values_button = QPushButton(self.frame)
        self.replace_values_button.setObjectName(u"replace_values_button")
        self.replace_values_button.setGeometry(QRect(125, 113, 200, 20))
        self.pick_game = QComboBox(self.centralwidget)
        self.pick_game.addItem("")
        self.pick_game.addItem("")
        self.pick_game.addItem("")
        self.pick_game.addItem("")
        self.pick_game.setObjectName(u"pick_game")
        self.pick_game.setGeometry(QRect(368, 50, 111, 23))
        self.pick_new_game = QComboBox(self.centralwidget)
        self.pick_new_game.addItem("")
        self.pick_new_game.addItem("")
        self.pick_new_game.addItem("")
        self.pick_new_game.addItem("")
        self.pick_new_game.setObjectName(u"pick_new_game")
        self.pick_new_game.setGeometry(QRect(830, 50, 111, 23))
        self.new_model_search = QLineEdit(self.centralwidget)
        self.new_model_search.setObjectName(u"new_model_search")
        self.new_model_search.setGeometry(QRect(490, 50, 331, 23))
        self.search_box = QLineEdit(self.centralwidget)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(30, 50, 331, 23))
        self.replace_height = QCheckBox(self.centralwidget)
        self.replace_height.setObjectName(u"replace_height")
        self.replace_height.setGeometry(QRect(500, 490, 171, 31))
        self.replace_all = QCheckBox(self.centralwidget)
        self.replace_all.setObjectName(u"replace_all")
        self.replace_all.setGeometry(QRect(810, 490, 171, 31))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 10, 931, 540))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        swap_values.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()
        self.model_list_label.raise_()
        self.save_button.raise_()
        self.model_list.raise_()
        self.revert_button.raise_()
        self.log_box.raise_()
        self.new_model_list.raise_()
        self.new_model_list_label.raise_()
        self.replace_btms_part.raise_()
        self.replace_tops_part.raise_()
        self.replace_hair_part.raise_()
        self.replace_face_part.raise_()
        self.pick_game.raise_()
        self.pick_new_game.raise_()
        self.new_model_search.raise_()
        self.search_box.raise_()
        self.replace_all.raise_()
        self.replace_face_flag.raise_()
        self.replace_tops_flag.raise_()
        self.replace_hair_flag.raise_()
        self.replace_btms_flag.raise_()
        self.replace_height.raise_()
        self.menubar = QMenuBar(swap_values)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 964, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        swap_values.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(swap_values)
        self.statusbar.setObjectName(u"statusbar")
        swap_values.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad_new_bin)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionSwapFlags)
        self.menuAbout.addAction(self.actionAbout_dmdEditor)

        self.retranslateUi(swap_values)

        QMetaObject.connectSlotsByName(swap_values)
    # setupUi

    def retranslateUi(self, swap_values):
        swap_values.setWindowTitle(QCoreApplication.translate("swap_values", u"dmdEditor", None))
        self.actionSettings.setText(QCoreApplication.translate("swap_values", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("swap_values", u"Exit", None))
        self.actionSwapFlags.setText(QCoreApplication.translate("swap_values", u"Use values from another model", None))
        self.actionSave.setText(QCoreApplication.translate("swap_values", u"Save", None))
        self.actionLoad_new_bin.setText(QCoreApplication.translate("swap_values", u"Load new .bin", None))
        self.actionAbout_dmdEditor.setText(QCoreApplication.translate("swap_values", u"About modeldata2", None))
        self.model_list_label.setText(QCoreApplication.translate("swap_values", u"Model list", None))
        self.save_button.setText(QCoreApplication.translate("swap_values", u"Save", None))
        self.revert_button.setText(QCoreApplication.translate("swap_values", u"Revert", None))
        self.log_box.setHtml(QCoreApplication.translate("swap_values", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program loaded.</p></body></html>", None))
        self.log_box.setPlaceholderText("")
        self.new_model_list_label.setText(QCoreApplication.translate("swap_values", u"Select the second model", None))
        self.replace_tops_flag.setText(QCoreApplication.translate("swap_values", u"Replace top flag", None))
        self.replace_face_flag.setText(QCoreApplication.translate("swap_values", u"Replace face flag", None))
        self.replace_hair_flag.setText(QCoreApplication.translate("swap_values", u"Replace hair flag", None))
        self.replace_btms_flag.setText(QCoreApplication.translate("swap_values", u"Replace bottom flag", None))
        self.replace_btms_part.setText(QCoreApplication.translate("swap_values", u"Replace bottom part", None))
        self.replace_tops_part.setText(QCoreApplication.translate("swap_values", u"Replace top part", None))
        self.replace_hair_part.setText(QCoreApplication.translate("swap_values", u"Replace hair part", None))
        self.replace_face_part.setText(QCoreApplication.translate("swap_values", u"Replace face part", None))
        self.replace_values_button.setText(QCoreApplication.translate("swap_values", u"Replace values", None))
        self.pick_game.setItemText(0, QCoreApplication.translate("swap_values", u"Yakuza Kiwami 2", None))
        self.pick_game.setItemText(1, QCoreApplication.translate("swap_values", u"Yakuza 6", None))
        self.pick_game.setItemText(2, QCoreApplication.translate("swap_values", u"Yakuza Like a Dragon", None))
        self.pick_game.setItemText(3, QCoreApplication.translate("swap_values", u"Judgment", None))

        self.pick_new_game.setItemText(0, QCoreApplication.translate("swap_values", u"Yakuza Kiwami 2", None))
        self.pick_new_game.setItemText(1, QCoreApplication.translate("swap_values", u"Yakuza 6", None))
        self.pick_new_game.setItemText(2, QCoreApplication.translate("swap_values", u"Yakuza Like a Dragon", None))
        self.pick_new_game.setItemText(3, QCoreApplication.translate("swap_values", u"Judgment", None))

        self.new_model_search.setPlaceholderText(QCoreApplication.translate("swap_values", u"Search...", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("swap_values", u"Search...", None))
        self.replace_height.setText(QCoreApplication.translate("swap_values", u"Replace height", None))
        self.replace_all.setText(QCoreApplication.translate("swap_values", u"Replace all", None))
        self.menuFile.setTitle(QCoreApplication.translate("swap_values", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("swap_values", u"Options", None))
        self.menuAbout.setTitle(QCoreApplication.translate("swap_values", u"About", None))
    # retranslateUi

