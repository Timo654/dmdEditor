# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_values.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_edit_values(object):
    def setupUi(self, edit_values):
        if not edit_values.objectName():
            edit_values.setObjectName(u"edit_values")
        edit_values.resize(968, 599)
        edit_values.setStyleSheet(u"QWidget\n"
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
        self.actionSettings = QAction(edit_values)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(edit_values)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSwapFlags = QAction(edit_values)
        self.actionSwapFlags.setObjectName(u"actionSwapFlags")
        self.actionSwapFlags.setCheckable(True)
        self.actionSave = QAction(edit_values)
        self.actionSave.setObjectName(u"actionSave")
        self.actionAbout_dmdEditor = QAction(edit_values)
        self.actionAbout_dmdEditor.setObjectName(u"actionAbout_dmdEditor")
        self.actionLoad_new_bin = QAction(edit_values)
        self.actionLoad_new_bin.setObjectName(u"actionLoad_new_bin")
        self.centralwidget = QWidget(edit_values)
        self.centralwidget.setObjectName(u"centralwidget")
        self.modellist_label = QLabel(self.centralwidget)
        self.modellist_label.setObjectName(u"modellist_label")
        self.modellist_label.setGeometry(QRect(30, 20, 131, 16))
        font = QFont()
        font.setPointSize(12)
        self.modellist_label.setFont(font)
        self.partflaginfo = QWidget(self.centralwidget)
        self.partflaginfo.setObjectName(u"partflaginfo")
        self.partflaginfo.setGeometry(QRect(520, 0, 431, 501))
        font1 = QFont()
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.partflaginfo.setFont(font1)
        self.partflaginfo.setAutoFillBackground(False)
        self.partflaginfo.setStyleSheet(u"")
        self.face_label = QLabel(self.partflaginfo)
        self.face_label.setObjectName(u"face_label")
        self.face_label.setGeometry(QRect(20, 20, 101, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.face_label.setFont(font2)
        self.height_label = QLabel(self.partflaginfo)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setGeometry(QRect(20, 420, 101, 21))
        self.height_label.setFont(font2)
        self.flag1_label = QLabel(self.partflaginfo)
        self.flag1_label.setObjectName(u"flag1_label")
        self.flag1_label.setGeometry(QRect(30, 80, 31, 21))
        self.value_label = QLabel(self.partflaginfo)
        self.value_label.setObjectName(u"value_label")
        self.value_label.setGeometry(QRect(30, 450, 28, 20))
        self.flag2_label = QLabel(self.partflaginfo)
        self.flag2_label.setObjectName(u"flag2_label")
        self.flag2_label.setGeometry(QRect(30, 180, 31, 16))
        self.part2_label = QLabel(self.partflaginfo)
        self.part2_label.setObjectName(u"part2_label")
        self.part2_label.setGeometry(QRect(30, 150, 31, 16))
        self.part4_label = QLabel(self.partflaginfo)
        self.part4_label.setObjectName(u"part4_label")
        self.part4_label.setGeometry(QRect(30, 350, 31, 16))
        self.flag4_label = QLabel(self.partflaginfo)
        self.flag4_label.setObjectName(u"flag4_label")
        self.flag4_label.setGeometry(QRect(30, 380, 31, 16))
        self.part1_label = QLabel(self.partflaginfo)
        self.part1_label.setObjectName(u"part1_label")
        self.part1_label.setGeometry(QRect(30, 50, 31, 16))
        self.part3_label = QLabel(self.partflaginfo)
        self.part3_label.setObjectName(u"part3_label")
        self.part3_label.setGeometry(QRect(30, 250, 31, 16))
        self.flag3_label = QLabel(self.partflaginfo)
        self.flag3_label.setObjectName(u"flag3_label")
        self.flag3_label.setGeometry(QRect(30, 280, 31, 16))
        self.tops_label = QLabel(self.partflaginfo)
        self.tops_label.setObjectName(u"tops_label")
        self.tops_label.setGeometry(QRect(20, 220, 81, 21))
        self.tops_label.setFont(font2)
        self.btms_label = QLabel(self.partflaginfo)
        self.btms_label.setObjectName(u"btms_label")
        self.btms_label.setGeometry(QRect(20, 320, 111, 21))
        self.btms_label.setFont(font2)
        self.hair_label = QLabel(self.partflaginfo)
        self.hair_label.setObjectName(u"hair_label")
        self.hair_label.setGeometry(QRect(20, 120, 101, 21))
        self.hair_label.setFont(font2)
        self.face_part = QLineEdit(self.partflaginfo)
        self.face_part.setObjectName(u"face_part")
        self.face_part.setGeometry(QRect(60, 50, 171, 23))
        self.face_part.setMaxLength(8)
        self.face_flag = QLineEdit(self.partflaginfo)
        self.face_flag.setObjectName(u"face_flag")
        self.face_flag.setGeometry(QRect(60, 80, 171, 23))
        self.face_flag.setMaxLength(16)
        self.hair_part = QLineEdit(self.partflaginfo)
        self.hair_part.setObjectName(u"hair_part")
        self.hair_part.setGeometry(QRect(60, 150, 171, 23))
        self.hair_part.setMaxLength(8)
        self.hair_flag = QLineEdit(self.partflaginfo)
        self.hair_flag.setObjectName(u"hair_flag")
        self.hair_flag.setGeometry(QRect(60, 180, 171, 23))
        self.hair_flag.setMaxLength(16)
        self.tops_part = QLineEdit(self.partflaginfo)
        self.tops_part.setObjectName(u"tops_part")
        self.tops_part.setGeometry(QRect(60, 250, 171, 23))
        self.tops_part.setMaxLength(8)
        self.tops_flag = QLineEdit(self.partflaginfo)
        self.tops_flag.setObjectName(u"tops_flag")
        self.tops_flag.setGeometry(QRect(60, 280, 171, 23))
        self.tops_flag.setMaxLength(16)
        self.btms_part = QLineEdit(self.partflaginfo)
        self.btms_part.setObjectName(u"btms_part")
        self.btms_part.setGeometry(QRect(60, 350, 171, 23))
        self.btms_part.setMaxLength(8)
        self.btms_flag = QLineEdit(self.partflaginfo)
        self.btms_flag.setObjectName(u"btms_flag")
        self.btms_flag.setGeometry(QRect(60, 380, 171, 23))
        self.btms_flag.setMaxLength(16)
        self.height_value = QLineEdit(self.partflaginfo)
        self.height_value.setObjectName(u"height_value")
        self.height_value.setGeometry(QRect(60, 450, 171, 23))
        self.height_value.setMaxLength(4)
        self.reset_defaults = QPushButton(self.partflaginfo)
        self.reset_defaults.setObjectName(u"reset_defaults")
        self.reset_defaults.setGeometry(QRect(270, 450, 121, 27))
        self.flagpart_frame = QFrame(self.partflaginfo)
        self.flagpart_frame.setObjectName(u"flagpart_frame")
        self.flagpart_frame.setGeometry(QRect(0, 10, 431, 491))
        self.flagpart_frame.setStyleSheet(u"")
        self.flagpart_frame.setFrameShape(QFrame.Box)
        self.flagpart_frame.setFrameShadow(QFrame.Raised)
        self.flagpart_frame.setLineWidth(1)
        self.line_5 = QFrame(self.flagpart_frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 90, 401, 20))
        self.line_5.setStyleSheet(u"")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.flagpart_frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(20, 190, 401, 20))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.flagpart_frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(20, 290, 401, 20))
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.flagpart_frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(20, 390, 401, 20))
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.tops_model = QComboBox(self.partflaginfo)
        self.tops_model.setObjectName(u"tops_model")
        self.tops_model.setGeometry(QRect(240, 250, 171, 23))
        self.tops_model.setEditable(True)
        self.tops_model.setFrame(True)
        self.btms_model = QComboBox(self.partflaginfo)
        self.btms_model.setObjectName(u"btms_model")
        self.btms_model.setGeometry(QRect(240, 350, 171, 23))
        self.btms_model.setEditable(True)
        self.btms_model.setFrame(True)
        self.hair_model = QComboBox(self.partflaginfo)
        self.hair_model.setObjectName(u"hair_model")
        self.hair_model.setGeometry(QRect(240, 150, 171, 23))
        self.hair_model.setEditable(True)
        self.hair_model.setFrame(True)
        self.face_model = QComboBox(self.partflaginfo)
        self.face_model.setObjectName(u"face_model")
        self.face_model.setGeometry(QRect(240, 50, 171, 23))
        self.face_model.setEditable(True)
        self.face_model.setFrame(True)
        self.is_decimal_height = QCheckBox(self.partflaginfo)
        self.is_decimal_height.setObjectName(u"is_decimal_height")
        self.is_decimal_height.setGeometry(QRect(60, 477, 211, 17))
        self.flagpart_frame.raise_()
        self.face_label.raise_()
        self.height_label.raise_()
        self.flag1_label.raise_()
        self.value_label.raise_()
        self.flag2_label.raise_()
        self.part2_label.raise_()
        self.part4_label.raise_()
        self.flag4_label.raise_()
        self.part1_label.raise_()
        self.part3_label.raise_()
        self.flag3_label.raise_()
        self.tops_label.raise_()
        self.btms_label.raise_()
        self.hair_label.raise_()
        self.face_part.raise_()
        self.face_flag.raise_()
        self.hair_part.raise_()
        self.hair_flag.raise_()
        self.tops_part.raise_()
        self.tops_flag.raise_()
        self.btms_part.raise_()
        self.btms_flag.raise_()
        self.height_value.raise_()
        self.reset_defaults.raise_()
        self.tops_model.raise_()
        self.btms_model.raise_()
        self.hair_model.raise_()
        self.face_model.raise_()
        self.is_decimal_height.raise_()
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setEnabled(True)
        self.save_button.setGeometry(QRect(840, 510, 101, 41))
        font3 = QFont()
        font3.setBold(False)
        self.save_button.setFont(font3)
        self.save_button.setAutoFillBackground(False)
        self.save_button.setCheckable(False)
        self.model_list = QListWidget(self.centralwidget)
        self.model_list.setObjectName(u"model_list")
        self.model_list.setGeometry(QRect(30, 80, 459, 387))
        self.model_list.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.revert_button = QPushButton(self.centralwidget)
        self.revert_button.setObjectName(u"revert_button")
        self.revert_button.setEnabled(True)
        self.revert_button.setGeometry(QRect(720, 510, 101, 41))
        self.revert_button.setFont(font3)
        self.revert_button.setAutoFillBackground(False)
        self.revert_button.setCheckable(False)
        self.log_box = QTextEdit(self.centralwidget)
        self.log_box.setObjectName(u"log_box")
        self.log_box.setGeometry(QRect(30, 466, 459, 23))
        self.log_box.setReadOnly(True)
        self.pick_game = QComboBox(self.centralwidget)
        self.pick_game.addItem("")
        self.pick_game.addItem("")
        self.pick_game.addItem("")
        self.pick_game.addItem("")
        self.pick_game.setObjectName(u"pick_game")
        self.pick_game.setGeometry(QRect(370, 50, 119, 23))
        self.searchBox = QLineEdit(self.centralwidget)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setGeometry(QRect(30, 50, 331, 23))
        self.searchBox.setMaxLength(100)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 501, 491))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        edit_values.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.partflaginfo.raise_()
        self.modellist_label.raise_()
        self.save_button.raise_()
        self.model_list.raise_()
        self.revert_button.raise_()
        self.log_box.raise_()
        self.pick_game.raise_()
        self.searchBox.raise_()
        self.menubar = QMenuBar(edit_values)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        edit_values.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(edit_values)
        self.statusbar.setObjectName(u"statusbar")
        edit_values.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad_new_bin)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionSwapFlags)
        self.menuAbout.addAction(self.actionAbout_dmdEditor)

        self.retranslateUi(edit_values)

        QMetaObject.connectSlotsByName(edit_values)
    # setupUi

    def retranslateUi(self, edit_values):
        edit_values.setWindowTitle(QCoreApplication.translate("edit_values", u"dmdEditor", None))
        self.actionSettings.setText(QCoreApplication.translate("edit_values", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("edit_values", u"Exit", None))
        self.actionSwapFlags.setText(QCoreApplication.translate("edit_values", u"Use values from another model", None))
        self.actionSave.setText(QCoreApplication.translate("edit_values", u"Save", None))
        self.actionAbout_dmdEditor.setText(QCoreApplication.translate("edit_values", u"About dmdEditor", None))
        self.actionLoad_new_bin.setText(QCoreApplication.translate("edit_values", u"Load new .bin", None))
        self.modellist_label.setText(QCoreApplication.translate("edit_values", u"Model list", None))
        self.face_label.setText(QCoreApplication.translate("edit_values", u"Head", None))
        self.height_label.setText(QCoreApplication.translate("edit_values", u"Height", None))
        self.flag1_label.setText(QCoreApplication.translate("edit_values", u"Flag", None))
        self.value_label.setText(QCoreApplication.translate("edit_values", u"Value", None))
        self.flag2_label.setText(QCoreApplication.translate("edit_values", u"Flag", None))
        self.part2_label.setText(QCoreApplication.translate("edit_values", u"Part", None))
        self.part4_label.setText(QCoreApplication.translate("edit_values", u"Part", None))
        self.flag4_label.setText(QCoreApplication.translate("edit_values", u"Flag", None))
        self.part1_label.setText(QCoreApplication.translate("edit_values", u"Part", None))
        self.part3_label.setText(QCoreApplication.translate("edit_values", u"Part", None))
        self.flag3_label.setText(QCoreApplication.translate("edit_values", u"Flag", None))
        self.tops_label.setText(QCoreApplication.translate("edit_values", u"Top", None))
        self.btms_label.setText(QCoreApplication.translate("edit_values", u"Bottom", None))
        self.hair_label.setText(QCoreApplication.translate("edit_values", u"Hair", None))
        self.reset_defaults.setText(QCoreApplication.translate("edit_values", u"Reset to default", None))
        self.is_decimal_height.setText(QCoreApplication.translate("edit_values", u"Use decimal for height (cm)", None))
        self.save_button.setText(QCoreApplication.translate("edit_values", u"Save", None))
        self.revert_button.setText(QCoreApplication.translate("edit_values", u"Revert", None))
        self.log_box.setHtml(QCoreApplication.translate("edit_values", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Program loaded.</span></p></body></html>", None))
        self.log_box.setPlaceholderText("")
        self.pick_game.setItemText(0, QCoreApplication.translate("edit_values", u"Yakuza Kiwami 2", None))
        self.pick_game.setItemText(1, QCoreApplication.translate("edit_values", u"Yakuza 6", None))
        self.pick_game.setItemText(2, QCoreApplication.translate("edit_values", u"Yakuza Like a Dragon", None))
        self.pick_game.setItemText(3, QCoreApplication.translate("edit_values", u"Judgment", None))

        self.searchBox.setPlaceholderText(QCoreApplication.translate("edit_values", u"Search...", None))
        self.menuFile.setTitle(QCoreApplication.translate("edit_values", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("edit_values", u"Options", None))
        self.menuAbout.setTitle(QCoreApplication.translate("edit_values", u"About", None))
    # retranslateUi

