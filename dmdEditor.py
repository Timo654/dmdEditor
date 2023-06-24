from ui_edit_values import Ui_edit_values
from ui_swap_values import Ui_swap_values
from ui_settings import Ui_Settings
from ui_about import Ui_About
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, QRegularExpression, Qt
from PySide6.QtGui import QRegularExpressionValidator, QPalette, QColor, QIcon
import os
import platform
from shutil import copyfile
import ctypes
import json
import sys
import struct
import binascii
import array
import pandas as pd

# saves file
def save_file(input_files, binary_data):
    # makes a copy of old file
    copyfile(input_files, input_files + '-old.bin')
    with open(input_files, 'wb') as f:
        f.write(binary_data)
        print(input_files + " saved.") 

# remembers table index
def set_table_index(self, table, window, model, model_second):
    global current_table1_selection
    global current_table2_selection
    main_table_count = len(df_main['character names'])
    try:
        second_table_count = len(df_second['character names'])
    except:
        pass

    if window == 'edit_values':
        model_list_model = self.ui.model_list.model()
        try:
            current_table1_selection
        except(NameError): # default is 0
            current_table1_selection = 0
        if model != None:
            current_table1_selection = model
        if current_table1_selection > main_table_count:
            current_table1_selection = 0
        current_model_index = model_list_model.index(current_table1_selection)
        self.ui.model_list.setCurrentIndex(current_model_index)
        
    if window == 'swap_values':
        if table == 'main':
            model_list_model = self.SV.model_list.model()
            if model != None:
                current_table1_selection = model
            if current_table1_selection > main_table_count:
                current_table1_selection = 0
            current_model_index = model_list_model.index(current_table1_selection)
            self.SV.model_list.setCurrentIndex(current_model_index)

        elif table == 'second':
            second_model_list_model = self.SV.new_model_list.model()
            try:
                current_table2_selection
            except(NameError): # default is 0
                current_table2_selection = 0
            if model_second != None:
                current_table2_selection = model_second
            if current_table2_selection > second_table_count:
                current_table2_selection = 0
            current_model2_index = second_model_list_model.index(current_table2_selection)
            self.SV.new_model_list.setCurrentIndex(current_model2_index)

# verifies input bin file
def verify_input_file(input_files):
    with open(input_files, 'rb') as binary_file:
        binary_data = bytearray(binary_file.read())
    try:
        if binary_data[0x00:0x04].decode().strip('\x00') == 'armp':
            return True
    except(UnicodeDecodeError):
        return False
    else:
        return False

# converts hex to int
def hex_to_int(value_to_convert, item_type):
    if item_type == 'part':
        Type = '<I'
    elif item_type == 'flag':
        Type = '<Q'
    elif item_type == 'height':
        Type = '<H'
    original_value = binascii.unhexlify(value_to_convert)
    y = array.array('h', original_value)
    s = struct.Struct(Type)
    little_endian_value = s.unpack_from(y)
    return int(little_endian_value[0])

# converts int to hex
def int_to_hex(value_to_convert, item_type):
    if item_type == 'part':
        Type = '<I'
    elif item_type == 'flag':
        Type = '<Q'
    elif item_type == 'height':
        Type = '<H'
    hex_value = binascii.hexlify(struct.pack(Type, value_to_convert)).decode('utf8')
    return hex_value

# gets offsets and values from modeldata table
def load_table(table_main):
    # list of columns that get loaded
    cols_list = ['character names', 'height', 'height offset', 'face', 'face offset', 'hair', 'hair offset', 'tops', 'tops offset', 'btms', 'btms offset', 'face_flags', 'face_flags offset', 'hair_flags', 'hair_flags offset', 'tops_flags', 'tops_flags offset', 'btms_flags', 'btms_flags offset']
    df = pd.read_csv(table_main, usecols=cols_list, delimiter=';') 
    return df
# gets values from parts table
def load_parts_table(table_parts):
    cols_list = ['parts','part id']
    df = pd.read_csv(table_parts, usecols=cols_list, delimiter=';') 
    return df

# quits the application
def exit_app():
    # saves log
    #sys.stdout.close()
    sys.exit()
# about window
class About(QMainWindow):
    def accept(self):
        self.close()
    def __init__(self):
        super(About, self).__init__()
        self.about= Ui_About()
        self.about.setupUi(self)
        # sets fixed window size
        self.setFixedSize(425, 300)
        # closes about window   
        self.about.pushButton.clicked.connect(self.accept) 

# settings
class Settings(QMainWindow):
    # select file
    def select_file(self, file, title):
        dialog = QFileDialog(self)
        dialog.setWindowTitle(title)
        dialog.selectFile(file)
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec():
            fileNames = dialog.selectedFiles()  
            return fileNames[0]
# TODO: use dict
    # select specific files
    def select_bin(self):
        title = "Select the model_data.bin file"
        selected_file = self.select_file('character_model_model_data.bin', title)
        return selected_file

    def select_lexus2(self):
        title = "Select the Kiwami 2 model_data table"
        selected_file = self.select_file('modeldata_lexus2.csv', title)
        if selected_file != None:
            self.settings.table_lexus2.setText(selected_file)
    def select_judge(self):
        title = "Select the Judgment model_data table"
        selected_file = self.select_file('modeldata_judge.csv', title)
        if selected_file != None:
            self.settings.table_judge.setText(selected_file)
    def select_ogref(self):
        title = "Select the Yakuza 6 model_data table"
        selected_file = self.select_file('modeldata_ogref.csv', title)
        if selected_file != None:
            self.settings.table_ogref.setText(selected_file)
    def select_persona(self):
        title = "Select the Yakuza Like a Dragon model_data table"
        selected_file = self.select_file('modeldata_persona.csv', title)
        if selected_file != None:
            self.settings.table_persona.setText(selected_file)
    def select_lexus2_parts(self):
        title = "Select the Kiwami 2 parts table"
        selected_file = self.select_file('parts_lexus2.csv', title)
        if selected_file != None:
            self.settings.table_lexus2_parts.setText(selected_file)
    def select_ogref_parts(self):
        title = "Select the Yakuza 6 parts table"
        selected_file = self.select_file('parts_ogref.csv', title)
        if selected_file != None:
            self.settings.table_ogref_parts.setText(selected_file)
    def select_judge_parts(self):
        title = "Select the Judgment parts table"
        selected_file = self.select_file('parts_judge.csv', title)
        if selected_file != None:
            self.settings.table_judge_parts.setText(selected_file)
    def select_persona_parts(self):
        title = "Select the Yakuza Like a Dragon parts table"
        selected_file = self.select_file('parts_persona.csv', title)
        if selected_file != None:
            self.settings.table_persona_parts.setText(selected_file)
    
    # shows dialog for reloading bin file
    def showDialog(self, settings):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Do you want to reload the last used bin file?")
        msgBox.setWindowTitle("dmdEditor")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            pass
        elif returnValue == QMessageBox.No:
            settings[0] = self.select_bin()
            # quit if no file is specified
            if settings[0] == None:
                sys.exit()
            else:
                self.save_settings_file(settings)
        elif returnValue == QMessageBox.Cancel:
            sys.exit()
    
    # saves settings
    def save_settings_file(self, settings):
        global binary_data
        with open(settings_file, 'w') as f:
                f.write(json.dumps(settings))
        input_files = settings[0]
        with open(input_files, 'rb') as binary_file:
            binary_data = bytearray(binary_file.read())

    # reads settings
    def read_settings_file(self):
        try:
            with open(settings_file, 'r') as f:
                settings = json.loads(f.read())
        except(json.decoder.JSONDecodeError):
            settings = ['\\', '.\\tables\\modeldata_lexus2.csv', '.\\tables\\modeldata_ogref.csv', '.\\tables\\modeldata_persona.csv', '.\\tables\\modeldata_judge.csv', '.\\tables\\parts_lexus2.csv', '.\\tables\\parts_ogref.csv', '.\\tables\\parts_persona.csv', '.\\tables\\parts_judge.csv', 0, 0]
        return settings

    # checks settings
    def check_settings(self, settings):
        if settings[0] == '\\':
            settings[0] = self.select_bin()
            self.save_settings_file(settings)
        else: self.showDialog(settings)

    # reads settings
    def read_settings(self, mode):
        global settings_file
        if os.name == 'nt':
            settings_folder = os.path.join(os.getenv('LOCALAPPDATA'), 'dmdEditor') #settings folder
        else: settings_folder = os.path.join(os.environ['HOME'], '.config', 'dmdEditor')
        if not os.path.exists(settings_folder):
            os.makedirs(settings_folder) 
        settings_file = os.path.join(settings_folder, 'settings.json') #settings file
        log_file = os.path.join(settings_folder, 'dmdEditor.log')
        if os.path.exists(log_file):
            copyfile(log_file, log_file[:-4] + '-old.log')
        sys.stdout = open(log_file, 'w')
        # making a settings file
        settings = []
        if os.path.exists(settings_file):
                settings = self.read_settings_file()
        else: settings = ['\\', '.\\tables\\modeldata_lexus2.csv', '.\\tables\\modeldata_ogref.csv', '.\\tables\\modeldata_persona.csv', '.\\tables\\modeldata_judge.csv', '.\\tables\\parts_lexus2.csv', '.\\tables\\parts_ogref.csv', '.\\tables\\parts_persona.csv', '.\\tables\\parts_judge.csv', 0, 0]

        if mode == 'default':
            self.settings.table_lexus2.setText(settings[1])
            self.settings.table_ogref.setText(settings[2])
            self.settings.table_persona.setText(settings[3])
            self.settings.table_judge.setText(settings[4])
            self.settings.table_lexus2_parts.setText(settings[5])
            self.settings.table_ogref_parts.setText(settings[6])
            self.settings.table_persona_parts.setText(settings[7])
            self.settings.table_judge_parts.setText(settings[8])
        return settings

    # save bin file
    def save(self, table_main_index, table_second_index):
        global input_files
        settings = self.read_settings_file()
        settings_new = [settings[0], self.settings.table_lexus2.text(), self.settings.table_ogref.text(), self.settings.table_persona.text(), self.settings.table_judge.text(), self.settings.table_lexus2_parts.text(), self.settings.table_ogref_parts.text(), self.settings.table_persona_parts.text(), self.settings.table_judge_parts.text(), table_main_index, table_second_index]
        self.save_settings_file(settings_new)
        print('settings saved')
        self.close()

    # selects new bin file
    def select_new_bin(self, settings):
        global input_files
        settings[0]= self.select_bin()
        # verify if input file is armp
        if settings[0] != None:
            while verify_input_file(settings[0]) == False:
                settings[0] = self.select_bin()
                if settings[0] == None:
                    break
                else:
                    verify_input_file(settings[0])
            else:
                self.save_settings_file(settings)
                input_files = settings[0]
                print('loaded new bin file')

    # closes settings
    def cancel(self):
        self.close()

    # resets settings to default
    def reset_to_default(self):
        self.settings.table_lexus2.setText('.\\tables\\modeldata_lexus2.csv')
        self.settings.table_ogref.setText('.\\tables\\modeldata_ogref.csv')
        self.settings.table_persona.setText('.\\tables\\modeldata_persona.csv')
        self.settings.table_judge.setText('.\\tables\\modeldata_judge.csv')
        self.settings.table_lexus2_parts.setText('.\\tables\\parts_lexus2.csv')
        self.settings.table_ogref_parts.setText('.\\tables\\parts_ogref.csv')
        self.settings.table_persona_parts.setText('.\\tables\\parts_persona.csv')
        self.settings.table_judge_parts.setText('.\\tables\\parts_judge.csv')
    def __init__(self, mode):
        super(Settings, self).__init__()
        self.settings = Ui_Settings()
        self.settings.setupUi(self)
        # set window size size
        self.setFixedSize(600, 655)

        # used on start for dialog
        settings = self.read_settings(mode)
        table_main_index = settings[9]
        table_second_index = settings[10]

        if mode == 'startup':
            self.check_settings(settings)
        if mode == 'new_bin':
            self.select_new_bin(settings)

        # select tables  
        self.settings.select_lexus2.clicked.connect(self.select_lexus2)
        self.settings.select_lexus2_parts.clicked.connect(self.select_lexus2_parts)
        self.settings.select_judge.clicked.connect(self.select_judge)
        self.settings.select_judge_parts.clicked.connect(self.select_judge_parts)
        self.settings.select_ogref.clicked.connect(self.select_ogref)
        self.settings.select_ogref_parts.clicked.connect(self.select_ogref_parts)
        self.settings.select_persona.clicked.connect(self.select_persona)
        self.settings.select_persona_parts.clicked.connect(self.select_persona_parts)

        # cancel
        self.settings.cancel_button_s.clicked.connect(self.cancel)

        # save settings
        self.settings.save_button_s.clicked.connect(lambda: self.save(table_main_index, table_second_index))

        # reset settings to default
        self.settings.default_button.clicked.connect(self.reset_to_default)

class swap_values(QMainWindow):
    # swaps values
    def swap_values(self):
        global binary_data
        model = df_main[df_main['character names'] == self.SV.model_list.currentItem().text()].index[0]
        model_new = df_second[df_second['character names'] == self.SV.new_model_list.currentItem().text()].index[0]
        if self.SV.replace_face_part.isChecked():   
            binary_data[df_main['face offset'].iloc[model]:df_main['face offset'].iloc[model]+4] = int(df_second['face'].iloc[model_new]).to_bytes(4, byteorder='little')
        if self.SV.replace_hair_part.isChecked():
            binary_data[df_main['hair offset'].iloc[model]:df_main['hair offset'].iloc[model]+4] = int(df_second['hair'].iloc[model_new]).to_bytes(4, byteorder='little')
        if self.SV.replace_tops_part.isChecked():
            binary_data[df_main['tops offset'].iloc[model]:df_main['tops offset'].iloc[model]+4] = int(df_second['tops'].iloc[model_new]).to_bytes(4, byteorder='little')
        if self.SV.replace_btms_part.isChecked():
            binary_data[df_main['btms offset'].iloc[model]:df_main['btms offset'].iloc[model]+4] = int(df_second['btms'].iloc[model_new]).to_bytes(4, byteorder='little')

        if self.SV.replace_face_flag.isChecked():
            binary_data[df_main['face_flags offset'].iloc[model]:df_main['face_flags offset'].iloc[model]+8] = int(df_second['face_flags'].iloc[model_new]).to_bytes(8, byteorder='little')
        if self.SV.replace_hair_flag.isChecked():
            binary_data[df_main['hair_flags offset'].iloc[model]:df_main['hair_flags offset'].iloc[model]+8] = int(df_second['hair_flags'].iloc[model_new]).to_bytes(8, byteorder='little')
        if self.SV.replace_tops_flag.isChecked():
            binary_data[df_main['tops_flags offset'].iloc[model]:df_main['tops_flags offset'].iloc[model]+8] = int(df_second['tops_flags'].iloc[model_new]).to_bytes(8, byteorder='little')
        if self.SV.replace_btms_flag.isChecked():
            binary_data[df_main['btms_flags offset'].iloc[model]:df_main['btms_flags offset'].iloc[model]+8] = int(df_second['btms_flags'].iloc[model_new]).to_bytes(8, byteorder='little')
        if self.SV.replace_height.isChecked():
            binary_data[df_main['height offset'].iloc[model]:df_main['height offset'].iloc[model]+2] = int(df_second['height'].iloc[model_new]).to_bytes(2, byteorder='little')
        self.SV.log_box.setText('Replaced values for ' + df_main['character names'].iloc[model] + '.')   
     
    # prevents from swapping parts if game is not the same
    def can_swap_parts(self):
        if int(self.SV.pick_game.currentIndex()) == int(self.SV.pick_new_game.currentIndex()):
            if self.SV.replace_all.isChecked():
                self.SV.replace_face_part.setChecked(True)
                self.SV.replace_hair_part.setChecked(True)
                self.SV.replace_tops_part.setChecked(True)
                self.SV.replace_btms_part.setChecked(True)
                self.SV.replace_face_part.setEnabled(False)
                self.SV.replace_hair_part.setEnabled(False)
                self.SV.replace_tops_part.setEnabled(False)
                self.SV.replace_btms_part.setEnabled(False)
            else:
                self.SV.replace_face_part.setEnabled(True)
                self.SV.replace_hair_part.setEnabled(True)
                self.SV.replace_tops_part.setEnabled(True)
                self.SV.replace_btms_part.setEnabled(True)
        else:
            self.SV.replace_face_part.setEnabled(False)
            self.SV.replace_hair_part.setEnabled(False)
            self.SV.replace_tops_part.setEnabled(False)
            self.SV.replace_btms_part.setEnabled(False)
            self.SV.replace_face_part.setChecked(False)
            self.SV.replace_hair_part.setChecked(False)
            self.SV.replace_tops_part.setChecked(False)
            self.SV.replace_btms_part.setChecked(False)

    # updates table
    def update_table(self, table_type):
        global df_main
        global df_second
        # save index to settings
        with open(settings_file, 'r') as f:
                settings = json.loads(f.read()) 
        settings[9] = self.SV.pick_game.currentIndex()
        settings[10] = self.SV.pick_new_game.currentIndex()
        with open(settings_file, 'w') as f:
            f.write(json.dumps(settings))
        try:
            if table_type == 'main' or table_type == 'both':
                self.SV.model_list.clear()
                if self.SV.pick_game.currentIndex() == 0:
                    table_main = open(settings[1])
    
                if self.SV.pick_game.currentIndex() == 1:
                    table_main = open(settings[2])
            
                if self.SV.pick_game.currentIndex() == 2:
                    table_main = open(settings[3])
            
                if self.SV.pick_game.currentIndex() == 3:
                    table_main = open(settings[4])
                df_main = load_table(table_main)
                self.SV.model_list.addItems(df_main['character names'])
                # filters 1st table search
                self.on_text_change(self.SV.new_model_search.text(), 'main')
                set_table_index(self, 'main', 'swap_values', None, None)
            if table_type == 'second' or table_type == 'both':
                self.SV.new_model_list.clear()
                if self.SV.pick_new_game.currentIndex() == 0:
                    table_second = open(settings[1])
    
                if self.SV.pick_new_game.currentIndex() == 1:
                    table_second = open(settings[2])
            
                if self.SV.pick_new_game.currentIndex() == 2:
                    table_second = open(settings[3])
            
                if self.SV.pick_new_game.currentIndex() == 3:
                    table_second = open(settings[4])
                df_second = load_table(table_second)
                self.SV.new_model_list.addItems(df_second['character names'])
                # filters 2nd table search
                self.on_text_change(self.SV.new_model_search.text(), 'second')
                set_table_index(self, 'second', 'swap_values', None, None)
            self.can_swap_parts()
            self.SV.log_box.setText('New table loaded successfully.')
        except(FileNotFoundError):
            self.SV.log_box.setText('One or more tables are missing.')

    # resets binary_data to default    
    def revert(self):
        global binary_data
        with open(input_files, 'rb') as binary_file:
            binary_data = bytearray(binary_file.read())
        self.SV.log_box.setText('Reverted to default.')
        self.SV.replace_all.setChecked(False)
        self.replace_all()

    # checks and unchecks checkboxes 
    def replace_all(self):
        if self.SV.replace_all.isChecked():
            if int(self.SV.pick_game.currentIndex()) == int(self.SV.pick_new_game.currentIndex()):
                self.SV.replace_face_part.setChecked(True)
                self.SV.replace_hair_part.setChecked(True)
                self.SV.replace_tops_part.setChecked(True)
                self.SV.replace_btms_part.setChecked(True)
            self.SV.replace_face_flag.setChecked(True)
            self.SV.replace_hair_flag.setChecked(True)
            self.SV.replace_tops_flag.setChecked(True)
            self.SV.replace_btms_flag.setChecked(True)
            self.SV.replace_height.setChecked(True)

            self.SV.replace_face_part.setEnabled(False)
            self.SV.replace_hair_part.setEnabled(False)
            self.SV.replace_tops_part.setEnabled(False)
            self.SV.replace_btms_part.setEnabled(False)
            self.SV.replace_face_flag.setEnabled(False)
            self.SV.replace_hair_flag.setEnabled(False)
            self.SV.replace_tops_flag.setEnabled(False)
            self.SV.replace_btms_flag.setEnabled(False)
            self.SV.replace_height.setEnabled(False)
        else:
            self.SV.replace_face_part.setChecked(False)
            self.SV.replace_hair_part.setChecked(False)
            self.SV.replace_tops_part.setChecked(False)
            self.SV.replace_btms_part.setChecked(False)
            self.SV.replace_face_flag.setChecked(False)
            self.SV.replace_hair_flag.setChecked(False)
            self.SV.replace_tops_flag.setChecked(False)
            self.SV.replace_btms_flag.setChecked(False)
            self.SV.replace_height.setChecked(False)

            if int(self.SV.pick_game.currentIndex()) == int(self.SV.pick_new_game.currentIndex()):
                self.SV.replace_face_part.setEnabled(True)
                self.SV.replace_hair_part.setEnabled(True)
                self.SV.replace_tops_part.setEnabled(True)
                self.SV.replace_btms_part.setEnabled(True)
            self.SV.replace_face_flag.setEnabled(True)
            self.SV.replace_hair_flag.setEnabled(True)
            self.SV.replace_tops_flag.setEnabled(True)
            self.SV.replace_btms_flag.setEnabled(True)
            self.SV.replace_height.setEnabled(True)

    # search
    def on_text_change(self, text, table_type):
        # replaces spaces with '_' for easier searching
        text = text.replace(' ', '_')
        if table_type == 'main':
            range_1 = self.SV.model_list.count()
            item = self.SV.model_list.item
        elif table_type == 'second':
            range_1 = self.SV.new_model_list.count()
            item = self.SV.new_model_list.item
        for row in range(range_1):
            it = item(row)
            text_list = text.lower().split('_') # make the search into a list
            included = True
            for t in text_list:
                if t:
                    if not self.text_filter(t, it.text().lower()):
                        included = False
                        break
            it.setHidden(not included)

    def text_filter(self, text, keywords):
        return text in keywords

    # about window
    def about(self):
        self.AB = About()
        self.AB.show()

    # settings window
    def settings(self):
        mode = 'default'
        self.ST = Settings(mode)
        self.ST.show()

    # goes to edit values window
    def edit_values(self):
        self.EV = edit_values()
        self.EV.show()
        self.close() 

    # select new bin   
    def select_new_bin(self):
        mode = 'new_bin'
        self.ST = Settings(mode)

    # saves file
    def save(self):
        save_file(input_files, binary_data)
        self.SV.log_box.setText('Saved bin file. Old file saved as ' + os.path.basename(input_files) + '-old.bin' )

    def selectionChanged(self, table):
        # saves new index
        if table == 'main':
            model = df_main[df_main['character names'] == self.SV.model_list.currentItem().text()].index[0]
            set_table_index(self, table, 'swap_values', model, None)
        elif table == 'second':
            model_second = df_second[df_second['character names'] == self.SV.new_model_list.currentItem().text()].index[0]
            set_table_index(self, table, 'swap_values', None, model_second)

    def __init__(self):
        global current_table2_selection
        super(swap_values, self).__init__()
        self.SV = Ui_swap_values()  
        self.SV.setupUi(self)
        # set fixed window size
        self.setFixedSize(964, 647)

        # load settings file
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                settings = json.loads(f.read())

        # loads table indexes from settings
        self.SV.pick_game.setCurrentIndex(settings[9])
        self.SV.pick_new_game.setCurrentIndex(settings[10])
        
        # updates both tables at startup
        self.update_table('both')

        # updates main table
        self.SV.pick_game.currentIndexChanged.connect(lambda: self.update_table('main'))

        # updates second table
        self.SV.pick_new_game.currentIndexChanged.connect(lambda: self.update_table('second'))

        # filters model list based on search box text
        self.SV.search_box.textChanged.connect(lambda: self.on_text_change(self.SV.search_box.text(), 'main'))
        self.SV.new_model_search.textChanged.connect(lambda: self.on_text_change(self.SV.new_model_search.text(), 'second'))

        # saves new index when selection is changed
        self.SV.model_list.itemSelectionChanged.connect(lambda: self.selectionChanged('main'))

        # saves new index when selection is changed
        self.SV.new_model_list.itemSelectionChanged.connect(lambda: self.selectionChanged('second'))

        # saves the file
        self.SV.actionSave.triggered.connect(self.save)
        self.SV.save_button.clicked.connect(self.save)

        # replaces values
        self.SV.replace_values_button.clicked.connect(self.swap_values)

        # hecks all checkboxes
        self.SV.replace_all.stateChanged.connect(self.replace_all)

        # resets the file
        self.SV.revert_button.clicked.connect(self.revert)

        # loads new bin file
        self.SV.actionLoad_new_bin.triggered.connect(self.select_new_bin)
        # opens about window
        self.SV.actionAbout_dmdEditor.triggered.connect(self.about)
        # opens edit values window
        self.SV.actionSwapFlags.triggered.connect(self.edit_values)
        # opens settings
        self.SV.actionSettings.triggered.connect(self.settings)
        # quits the application
        self.SV.actionExit.triggered.connect(exit_app)

#edit values mode
class edit_values(QMainWindow):
    #opens swap_values window
    def swap_values(self):
        self.SV = swap_values()
        self.SV.show()
        self.close()
    # opens settings window
    def settings(self):
        mode = 'default'
        self.ST = Settings(mode)
        self.ST.show()

    # opens about window
    def about(self):
        self.AB = About()
        self.AB.show()

    # update part name in combobox based on value
    def update_parts(self, mode):
        if len(self.ui.face_part.text()) == 8 and mode == 'face' or mode == 'all': 
            try:
                if self.ui.pick_game.currentText() == 'Judgment' and hex_to_int(self.ui.face_part.text(), 'part') == 0:
                    self.ui.face_model.setCurrentText('none')
                else:
                    face_number = df_parts[df_parts['part id'] == hex_to_int(self.ui.face_part.text(), 'part')].index[0]
                    self.ui.face_model.setCurrentIndex(face_number)
            except(ValueError, IndexError):
                self.ui.face_model.setCurrentText('none')
        if len(self.ui.hair_part.text()) == 8 and mode == 'hair' or mode == 'all': 
            try:
                if self.ui.pick_game.currentText() == 'Judgment' and hex_to_int(self.ui.hair_part.text(), 'part') == 0:
                    self.ui.hair_model.setCurrentText('none')
                else:
                    hair_number = df_parts[df_parts['part id'] == hex_to_int(self.ui.hair_part.text(), 'part')].index[0]
                    self.ui.hair_model.setCurrentIndex(hair_number)
            except(ValueError, IndexError):
                self.ui.hair_model.setCurrentText('none')
        if len(self.ui.tops_part.text()) == 8 and mode == 'tops' or mode == 'all':
            try:
                if self.ui.pick_game.currentText() == 'Judgment' and hex_to_int(self.ui.tops_part.text(), 'part') == 0:
                    self.ui.tops_model.setCurrentText('none')
                else:
                    tops_number = df_parts[df_parts['part id'] == hex_to_int(self.ui.tops_part.text(), 'part')].index[0]
                    self.ui.tops_model.setCurrentIndex(tops_number)
            except(ValueError, IndexError):
                self.ui.tops_model.setCurrentText('none')
        if len(self.ui.btms_part.text()) == 8 and mode == 'btms' or mode == 'all': 
            try:
                if self.ui.pick_game.currentText() == 'Judgment' and hex_to_int(self.ui.btms_part.text(), 'part') == 0:
                    self.ui.btms_model.setCurrentText('none')
                else:
                    btms_number = df_parts[df_parts['part id'] == hex_to_int(self.ui.btms_part.text(), 'part')].index[0]
                    self.ui.btms_model.setCurrentIndex(btms_number)
            except(ValueError, IndexError):
                self.ui.btms_model.setCurrentText('none')

    # updates table
    def update_table(self):
        global df_main
        global df_parts
        
        # loads settings
        with open(settings_file, 'r') as f:
                settings = json.loads(f.read())
        settings[9] = self.ui.pick_game.currentIndex()
        # saves current selected game index
        with open(settings_file, 'w') as f:
            f.write(json.dumps(settings))

        # clears model list
        self.ui.model_list.clear()
        try:
            if self.ui.pick_game.currentIndex() == 0:
                table = open(settings[1])
                table_parts = open(settings[5])
            if self.ui.pick_game.currentIndex() == 1:
                table = open(settings[2])
                table_parts = open(settings[6])
            if self.ui.pick_game.currentIndex() == 2:
                table = open(settings[3])
                table_parts = open(settings[7])
            if self.ui.pick_game.currentIndex() == 3:
                table = open(settings[4])
                table_parts = open(settings[8])
            df_main = load_table(table)
            df_parts = load_parts_table(table_parts)
            self.ui.model_list.addItems(df_main['character names'])

            # clears comboboxes
            self.ui.face_model.clear()
            self.ui.hair_model.clear()
            self.ui.tops_model.clear()
            self.ui.btms_model.clear()

            # adds items to combobox
            self.ui.face_model.addItems(df_parts['parts'])
            self.ui.hair_model.addItems(df_parts['parts'])
            self.ui.tops_model.addItems(df_parts['parts'])
            self.ui.btms_model.addItems(df_parts['parts'])

            #filters based on search
            self.on_text_change(self.ui.searchBox.text())
            set_table_index(self, 'main', 'edit_values', None, None)
            self.ui.log_box.setText('New table loaded successfully.')
        except(FileNotFoundError):
            self.ui.log_box.setText('One or more tables are missing.')

    # update values
    def selectionChanged(self):
        try:
            model = df_main[df_main['character names'] == self.ui.model_list.currentItem().text()].index[0]
            # saves model index
            set_table_index(self, 'main', 'edit_values', model, None)

            # parts
            self.ui.face_part.setText(int_to_hex(int.from_bytes(binary_data[df_main['face offset'].iloc[model]:df_main['face offset'].iloc[model]+4], 'little'), 'part'))
            self.ui.hair_part.setText(int_to_hex(int.from_bytes(binary_data[df_main['hair offset'].iloc[model]:df_main['hair offset'].iloc[model]+4], 'little'), 'part'))
            self.ui.tops_part.setText(int_to_hex(int.from_bytes(binary_data[df_main['tops offset'].iloc[model]:df_main['tops offset'].iloc[model]+4], 'little'), 'part'))
            self.ui.btms_part.setText(int_to_hex(int.from_bytes(binary_data[df_main['btms offset'].iloc[model]:df_main['btms offset'].iloc[model]+4], 'little'), 'part'))

            # flags
            self.ui.face_flag.setText(int_to_hex(int.from_bytes(binary_data[df_main['face_flags offset'].iloc[model]:df_main['face_flags offset'].iloc[model]+8], 'little'), 'flag'))
            self.ui.hair_flag.setText(int_to_hex(int.from_bytes(binary_data[df_main['hair_flags offset'].iloc[model]:df_main['hair_flags offset'].iloc[model]+8], 'little'), 'flag'))
            self.ui.tops_flag.setText(int_to_hex(int.from_bytes(binary_data[df_main['tops_flags offset'].iloc[model]:df_main['tops_flags offset'].iloc[model]+8], 'little'), 'flag'))
            self.ui.btms_flag.setText(int_to_hex(int.from_bytes(binary_data[df_main['btms_flags offset'].iloc[model]:df_main['btms_flags offset'].iloc[model]+8], 'little'), 'flag'))
            # height
            if self.ui.is_decimal_height.isChecked():
                self.ui.height_value.setText(str(int.from_bytes(binary_data[df_main['height offset'].iloc[model]:df_main['height offset'].iloc[model]+2], 'little')))
            else:
                self.ui.height_value.setText(int_to_hex(int.from_bytes(binary_data[df_main['height offset'].iloc[model]:df_main['height offset'].iloc[model]+2], 'little'), 'height'))

            self.update_parts('all')
        except(AttributeError):
            self.ui.log_box.setText('Select a model.')
        except(NameError):
            self.ui.log_box.setText('Select a table.')

    # load part value based on combobox option
    def load_from_part_name(self, part):
        part_numbers = df_parts['part id']
        try:
            if part == 'face':
                face_number = self.ui.face_model.currentIndex()
                self.ui.face_part.setText(int_to_hex(part_numbers[face_number], 'part'))
            if part == 'hair':
                hair_number = self.ui.hair_model.currentIndex()
                self.ui.hair_part.setText(int_to_hex(part_numbers[hair_number], 'part'))
            if part == 'tops':
                tops_number = self.ui.tops_model.currentIndex()
                self.ui.tops_part.setText(int_to_hex(part_numbers[tops_number], 'part'))
            if part == 'btms':
                btms_number = self.ui.btms_model.currentIndex()
                self.ui.btms_part.setText(int_to_hex(part_numbers[btms_number], 'part'))
            if part == 'face' or part == 'hair' or part == 'tops' or part == 'btms':
                self.auto_save()
        except(KeyError):
            pass

    # search
    def on_text_change(self, text):
    # replaces spaces with '_' for easier searching
        text = text.replace(' ', '_')
        for row in range(self.ui.model_list.count()):
            it = self.ui.model_list.item(row)
            text_list = text.lower().split('_') # turns it to a list
            included = True
            for t in text_list:
                if t:
                    if not self.text_filter(t, it.text().lower()):
                        included = False
                        break
            it.setHidden(not included)

    def text_filter(self, text, keywords):
        return text in keywords
        

    # disable usage of non hex characters
    def validate_input(self, decimal_height):
        reg_ex = QRegularExpression('^[a-fA-F0-9]*$')
        input_validator = QRegularExpressionValidator(reg_ex)
        height_validator = QRegularExpressionValidator(QRegularExpression('^[0-9]*$'))

        self.ui.face_part.setValidator(input_validator)
        self.ui.hair_part.setValidator(input_validator)
        self.ui.tops_part.setValidator(input_validator)
        self.ui.btms_part.setValidator(input_validator)

        self.ui.face_flag.setValidator(input_validator)
        self.ui.hair_flag.setValidator(input_validator)
        self.ui.tops_flag.setValidator(input_validator)
        self.ui.btms_flag.setValidator(input_validator)
        if decimal_height == True:
            self.ui.height_value.setValidator(height_validator)
        else:
            self.ui.height_value.setValidator(input_validator)

    # convert height to decimal
    def height_to_decimal(self):
        if self.ui.is_decimal_height.isChecked():
            decimal_height = True
            self.ui.height_value.setMaxLength(5)
        else:
            decimal_height = False
            self.ui.height_value.setMaxLength(4)
        self.validate_input(decimal_height)
        self.selectionChanged()

    # reset values to default based on the values in the table
    def reset_defaults(self):
        try:
            model = df_main[df_main['character names'] == self.ui.model_list.currentItem().text()].index[0] 
            self.ui.face_part.setText(int_to_hex(df_main['face'].iloc[model], 'part'))
            self.ui.face_flag.setText(int_to_hex(df_main['face_flags'].iloc[model], 'flag'))

            self.ui.hair_part.setText(int_to_hex(df_main['hair'].iloc[model], 'part'))
            self.ui.hair_flag.setText(int_to_hex(df_main['hair_flags'].iloc[model], 'flag'))

            self.ui.tops_part.setText(int_to_hex(df_main['tops'].iloc[model], 'part'))
            self.ui.tops_flag.setText(int_to_hex(df_main['tops_flags'].iloc[model], 'flag'))

            self.ui.btms_part.setText(int_to_hex(df_main['btms'].iloc[model], 'part'))
            self.ui.btms_flag.setText(int_to_hex(df_main['btms_flags'].iloc[model], 'flag'))
        
            if self.ui.is_decimal_height.isChecked():
                self.ui.height_value.setText(str(df_main['height'].iloc[model]))
            else:
                self.ui.height_value.setText(int_to_hex(df_main['height'].iloc[model], 'height'))
            self.update_parts('all')
            self.ui.log_box.setText('Reset values for ' + df_main['character names'].iloc[model] + '.')
            self.auto_save()
        except(AttributeError):
            self.ui.log_box.setText("Can't reset values if no model is selected.")

    # loads new bin file
    def select_new_bin(self):
        mode = 'new_bin'
        self.ST = Settings(mode)

    # reverts binary_data to default
    def revertButton(self, input_files):
        global binary_data
        with open(input_files, 'rb') as binary_file:
            binary_data = bytearray(binary_file.read())
        self.selectionChanged()
        self.ui.log_box.setText('Reverted to default.')
    
    # saves edited file in memory
    def auto_save(self):
        global binary_data
        try:
            # get current model
            model = df_main[df_main['character names'] == self.ui.model_list.currentItem().text()].index[0]
            if len(self.ui.face_part.text()) == 8:
                binary_data[df_main['face offset'].iloc[model]:df_main['face offset'].iloc[model]+4] = hex_to_int(self.ui.face_part.text(), 'part').to_bytes(4, byteorder='little')
            if len(self.ui.hair_part.text()) == 8:
                binary_data[df_main['hair offset'].iloc[model]:df_main['hair offset'].iloc[model]+4] = hex_to_int(self.ui.hair_part.text(), 'part').to_bytes(4, byteorder='little')
            if len(self.ui.tops_part.text()) == 8:
                binary_data[df_main['tops offset'].iloc[model]:df_main['tops offset'].iloc[model]+4] = hex_to_int(self.ui.tops_part.text(), 'part').to_bytes(4, byteorder='little')
            if len(self.ui.btms_part.text()) == 8:
                binary_data[df_main['btms offset'].iloc[model]:df_main['btms offset'].iloc[model]+4] = hex_to_int(self.ui.btms_part.text(), 'part').to_bytes(4, byteorder='little')
            if len(self.ui.face_flag.text()) == 16:
                binary_data[df_main['face_flags offset'].iloc[model]:df_main['face_flags offset'].iloc[model]+8] = hex_to_int(self.ui.face_flag.text(), 'flag').to_bytes(8, byteorder='little')
            if len(self.ui.hair_flag.text()) == 16:
                binary_data[df_main['hair_flags offset'].iloc[model]:df_main['hair_flags offset'].iloc[model]+8] = hex_to_int(self.ui.hair_flag.text(), 'flag').to_bytes(8, byteorder='little')
            if len(self.ui.tops_flag.text()) == 16:
                binary_data[df_main['tops_flags offset'].iloc[model]:df_main['tops_flags offset'].iloc[model]+8] = hex_to_int(self.ui.tops_flag.text(), 'flag').to_bytes(8, byteorder='little')
            if len(self.ui.btms_flag.text()) == 16:
                binary_data[df_main['btms_flags offset'].iloc[model]:df_main['btms_flags offset'].iloc[model]+8] = hex_to_int(self.ui.btms_flag.text(), 'flag').to_bytes(8, byteorder='little')
            if self.ui.is_decimal_height.isChecked():
                # if value is too big, sets to the highest possible value
                if int(self.ui.height_value.text()) > 65535:
                    self.ui.height_value.setText('65535')
                binary_data[df_main['height offset'].iloc[model]:df_main['height offset'].iloc[model]+2] = int(self.ui.height_value.text()).to_bytes(2, byteorder='little')
            elif len(self.ui.height_value.text()) == 4:
                binary_data[df_main['height offset'].iloc[model]:df_main['height offset'].iloc[model]+2] = hex_to_int(self.ui.height_value.text(), 'height').to_bytes(2, byteorder='little')
        except(AttributeError):
            pass

    # saves file
    def save(self):
        save_file(input_files, binary_data)
        self.ui.log_box.setText('Saved bin file. Old file saved as ' + os.path.basename(input_files) + '-old.bin' )
    
    def __init__(self):
        global input_files
        global binary_data

        super(edit_values, self).__init__()

        self.ui = Ui_edit_values()
        self.ui.setupUi(self)

        # sets fixed window size
        self.setFixedSize(964, 600)

        # fixes combobox ui
        self.ui.pick_game.setStyleSheet('''*    QComboBox QAbstractItemView {min-width: 150px;}''')

        # read settings
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                settings = json.loads(f.read())
        input_files = settings[0]

        try:
            binary_data
        except(NameError):
            try:
                with open(input_files, 'rb') as binary_file:
                    binary_data = bytearray(binary_file.read())
                    if verify_input_file(input_files) == False:
                        self.select_new.bin()
            except: self.select_new_bin()
        else: pass

        # updates model list table on startup
        self.update_table()

        # updates model list table when table is changed
        self.ui.pick_game.currentIndexChanged.connect(self.update_table)

        # updates selected game index based on saved value
        self.ui.pick_game.setCurrentIndex(settings[9])

        # validates input, decimal height = False
        self.validate_input(False)

        # convert hex height to decimal
        self.ui.is_decimal_height.stateChanged.connect(self.height_to_decimal)

        # updates values on startup
        self.selectionChanged()

        # updates values on selection change
        self.ui.model_list.itemSelectionChanged.connect(self.selectionChanged)


        # reverts edited binary_data to default
        self.ui.revert_button.clicked.connect(lambda: self.revertButton(input_files))
        
        # resets values to default based on the table
        self.ui.reset_defaults.clicked.connect(self.reset_defaults)

        # update part index in combobox when editing value
        self.ui.face_part.textEdited.connect(lambda: self.update_parts('face'))
        self.ui.hair_part.textEdited.connect(lambda: self.update_parts('hair'))
        self.ui.tops_part.textEdited.connect(lambda: self.update_parts('tops'))
        self.ui.btms_part.textEdited.connect(lambda: self.update_parts('btms'))

        # update part value when picking from combobox
        self.ui.face_model.currentIndexChanged.connect(lambda: self.load_from_part_name('face'))
        self.ui.hair_model.currentIndexChanged.connect(lambda: self.load_from_part_name('hair'))
        self.ui.tops_model.currentIndexChanged.connect(lambda: self.load_from_part_name('tops'))
        self.ui.btms_model.currentIndexChanged.connect(lambda: self.load_from_part_name('btms'))

        # filters text based on text in search box
        self.ui.searchBox.textChanged.connect(self.on_text_change)

        # save file
        self.ui.save_button.clicked.connect(self.save)
        self.ui.actionSave.triggered.connect(self.save)

        # autosaving to memory
        self.ui.face_part.textEdited.connect(self.auto_save)
        self.ui.hair_part.textEdited.connect(self.auto_save)
        self.ui.tops_part.textEdited.connect(self.auto_save)
        self.ui.btms_part.textEdited.connect(self.auto_save)

        self.ui.face_flag.textEdited.connect(self.auto_save)
        self.ui.hair_flag.textEdited.connect(self.auto_save)
        self.ui.tops_flag.textEdited.connect(self.auto_save)
        self.ui.btms_flag.textEdited.connect(self.auto_save)
        self.ui.height_value.textEdited.connect(self.auto_save)

        # opens settings
        self.ui.actionSettings.triggered.connect(self.settings)

        # about window button
        self.ui.actionAbout_dmdEditor.triggered.connect(self.about)

        # swap values window
        self.ui.actionSwapFlags.triggered.connect(self.swap_values)

        # loads new bin file
        self.ui.actionLoad_new_bin.triggered.connect(self.select_new_bin)

        # quits the application
        self.ui.actionExit.triggered.connect(exit_app)

if __name__ == "__main__":
    # makes it not dpi aware, because it breaks the UI otherwise
    # TODO - verify if this is still needed
    #if os.name == 'nt':
    #    ctypes.windll.user32.SetProcessDPIAware()

    app = QApplication(sys.argv)
    
    #sets icon
    app.setWindowIcon(QIcon("dmd.ico"))

    # style related stuff
    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    # loads settings and asks for files
    ST = Settings('startup')

    # opens edit values window
    window = edit_values()
    window.show()

    sys.exit(app.exec())