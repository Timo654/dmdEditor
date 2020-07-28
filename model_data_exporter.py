import math
import struct
import argparse
import sys
import pandas as pd

#override arguments for testing/debug purposes
override_args = False

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",  help='Input file (model_data.bin)', type=str)
parser.add_argument("-g", "--game", help="Pick a game. Possible choices are 'lexus2' (Kiwami 2), 'ogref' (Yakuza 6) and 'judge' (Judgment).", type=str)
args = parser.parse_args()


if override_args == True:
    #override input
    args.input = 'character_model_model_data_judges.bin'
    #override game
    args.game = 'lexus2'
else:
#quit if no arguments are used
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

#input file
input_files = args.input
#game where the file is from
game = args.game

#load input file
with open(input_files, 'rb') as binary_file:
        binary_data = bytearray(binary_file.read())

model_count = int.from_bytes(binary_data[0x20:0x24], 'little')
first_table =  int.from_bytes(binary_data[0x10:0x14], 'little')

def get_names(data, item_count, item_list_offset):
    # Number of names
    n = item_count

    # obtain the first name location
    p = item_list_offset
    starting_addr = struct.unpack('<i', data[p:p+4])[0]

    names = []

    # buffer to read one name at the time
    curr_name = ''

    # curr_p will be moving until it founds a 0x0 char
    curr_p = starting_addr
    for _ in range(n):

        # add to buffer until it finds a terminator symbol (0x0)
        while data[curr_p] != 0x0:
            curr_name += chr(data[curr_p])
            curr_p += 1

        # append the name in buffer then clean it
        names.append(curr_name)
        curr_name = ''
        curr_p += 1
    return names

def get_model_names(binary_data, model_count):
    #get model names
    global df
    model_list_offset = int.from_bytes(binary_data[0x30:0x34], 'little')
    model_names = get_names(binary_data, model_count, model_list_offset)
    model_list_offset_end = model_list_offset + (model_count - 1) * 4
    df = pd.DataFrame()
    df['character names'] = model_names
    df.to_csv('modeldata_' + game + '.csv',sep=';', encoding='utf8', index=False)
    get_puid_order(binary_data, model_count, model_list_offset_end)

def get_puid_order(binary_data, model_count, model_list_offset_end):
    #diff is the difference between offsets
    if game == 'judge' or game == 'ogref':
        puid_order_start_offset = int.from_bytes(binary_data[first_table-24:first_table-20], 'little')
    elif game == 'lexus2':
        puid_order_start_offset = int.from_bytes(binary_data[first_table-16:first_table-12], 'little')

    puid_order_offsets = [puid_order_start_offset]
    puid_order_list = []
    for i in range(0, model_count):
        puid_order = int.from_bytes(binary_data[puid_order_start_offset:puid_order_start_offset+4], 'little')
        puid_order_list.append(puid_order)
        if i != model_count - 1:
            puid_order_start_offset += 4
            puid_order_offsets.append(puid_order_start_offset)
    df['puid order'] = puid_order_list
    df['puid_order offset'] = puid_order_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_model_name_order(binary_data, model_count, puid_order_start_offset)
    
def get_model_name_order(binary_data, model_count, puid_order_start_offset):
    curr_p = puid_order_start_offset + 4
    while binary_data[curr_p] == 0:
        curr_p += 1
    model_name_order_start_offset = curr_p
    model_name_order_offsets = [model_name_order_start_offset]
    model_name_order_list = []
    for i in range(0, model_count):
        model_name_order = int.from_bytes(binary_data[model_name_order_start_offset:model_name_order_start_offset+4], 'little')
        model_name_order_list.append(model_name_order)
        if i != model_count - 1:
            model_name_order_start_offset += 4
            model_name_order_offsets.append(model_name_order_start_offset)
    df['character order'] = model_name_order_list
    df['character order offset'] = model_name_order_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_part_names(binary_data, model_count, model_name_order_start_offset)

def get_part_names(binary_data, model_count, model_name_order_start_offset):
    #get part names
    diff = 8
    part_count_start = first_table + diff
    part_list_start = part_count_start + 28
    part_count = int.from_bytes(binary_data[part_count_start:part_count_start+4], 'little')
    part_list_offset = int.from_bytes(binary_data[part_list_start:part_list_start+4], 'little')
    part_names = get_names(binary_data, part_count, part_list_offset)
    part_list_offset_end = part_list_offset + (part_count - 1) * 4 
    df2 = pd.DataFrame()
    df2['parts'] = part_names
    df2.to_csv('parts_' + game + '.csv',sep=';', index=False)   
    get_part_order(binary_data, model_count, part_list_offset_end, part_count, df2)

def get_part_order(binary_data, model_count, part_list_offset_end, part_count, df2):
    part_order_list = []
    part_nr = 0
    for i in range(0, part_count):
        part_order_list.append(part_nr)
        part_nr += 1
    df2['part id'] = part_order_list
    df2.to_csv('parts_' + game + '.csv',sep=';', index=False) 
    get_value(binary_data, model_count)

def get_value(binary_data, model_count):
    another_table = int.from_bytes(binary_data[first_table+24:first_table+28], 'little')
    if game == 'judge':
        diff = 46
    elif game == 'lexus2':
        diff = 90
    elif game == 'ogref':
        diff = 88
    value_start_offset = another_table + diff
    value_offsets = [value_start_offset]
    values_list = []
    for i in range(0, model_count):
        value = int.from_bytes(binary_data[value_start_offset:value_start_offset+2], 'little')
        values_list.append(value)
        if i != model_count - 1:
            value_start_offset += 2
            value_offsets.append(value_start_offset)
    if game == 'lexus2' or game == 'judge':
        df['*model'] = values_list
        df['*model offset'] = value_offsets
    elif game == 'ogref':
        df['*character'] = values_list
        df['*character offset'] = value_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    df.sort_values(by=['character order'], inplace=True)
    if game == 'judge' or game == 'ogref':
        get_category(binary_data, model_count, value_start_offset)
    elif game == 'lexus2':
        get_is_reuse(binary_data, model_count, value_start_offset)

def get_is_reuse(binary_data, model_count, value_start_offset):
    #unused in judgment
    if game == 'lexus2':
        is_reuse_start_offset = value_start_offset + 6
    elif game == 'ogref':
        is_reuse_start_offset = value_start_offset + 4
    is_reuse_offsets = []
    is_reuse_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        is_reuse = list(f'{binary_data[is_reuse_start_offset]:0>8b}')
        is_reuse.reverse()
        for data in is_reuse:
            if (model_iterator == model_count):
                break
            else:  
                is_reuse_list.append(data)
                is_reuse_offsets.append(is_reuse_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1:
            is_reuse_start_offset += 1
        
    df['is_reuse'] = is_reuse_list
    df['is_reuse offset'] = is_reuse_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'lexus2': 
        get_category(binary_data, model_count, is_reuse_start_offset)

def get_category(binary_data, model_count, is_reuse_start_offset):
    if game == 'judge':
        diff = 6
    elif game == 'lexus2':
        diff = 1
    elif game == 'ogref':
        diff = 4
    category_start_offset = is_reuse_start_offset + diff
    category_offsets = [category_start_offset]
    category_list = []
    for i in range(0, model_count):
        category = binary_data[category_start_offset]
        category_list.append(category)
        if i != model_count - 1:
            category_start_offset += 1
            category_offsets.append(category_start_offset)
        
    df['category'] = category_list
    df['category offset'] = category_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_class_id(binary_data, model_count, category_start_offset)

def get_class_id(binary_data, model_count, category_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    class_id_start_offset = category_start_offset + diff
    class_id_offsets = [class_id_start_offset]
    class_id_list = []
    for i in range(0, model_count):
        class_id = binary_data[class_id_start_offset]
        class_id_list.append(class_id)
        if i != model_count - 1:
            class_id_start_offset += 1
            class_id_offsets.append(class_id_start_offset)
        
    df['class id'] = class_id_list
    df['class id offset'] = class_id_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_age(binary_data, model_count, class_id_start_offset)

def get_age(binary_data, model_count, class_id_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    age_start_offset = class_id_start_offset + diff
    age_offsets = [age_start_offset]
    age_list = []
    for i in range(0, model_count):
        age = binary_data[age_start_offset]
        age_list.append(age)
        if i != model_count - 1:
            age_start_offset += 1
            age_offsets.append(age_start_offset)
        
    df['age'] = age_list
    df['age offset'] = age_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_is_woman(binary_data, model_count, age_start_offset)

def get_is_woman(binary_data, model_count, age_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    is_woman_start_offset = age_start_offset + diff
    is_woman_offsets = []
    is_woman_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        is_woman = list(f'{binary_data[is_woman_start_offset]:0>8b}')
        is_woman.reverse()
        for data in is_woman:
            if (model_iterator == model_count):
                break
            else:  
                is_woman_list.append(data)
                is_woman_offsets.append(is_woman_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1:
            is_woman_start_offset += 1
        
    df['is_woman'] = is_woman_list
    df['is_woman offset'] = is_woman_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'lexus2' or game == 'judge': 
        get_is_face_correct(binary_data, model_count, is_woman_start_offset)
    elif game == 'ogref':
        get_height(binary_data, model_count, is_woman_start_offset)

def get_is_face_correct(binary_data, model_count, is_woman_start_offset):
    if game == 'judge':
        diff = 4
    elif game == 'lexus2':
        diff = 1
    elif game == 'ogref':
        diff = 2
    is_face_correct_start_offset = is_woman_start_offset + diff
    is_face_correct_offsets = []
    is_face_correct_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        is_face_correct = list(f'{binary_data[is_face_correct_start_offset]:0>8b}')
        is_face_correct.reverse()
        for data in is_face_correct:
            if (model_iterator == model_count):
                break
            else:  
                is_face_correct_list.append(data)
                is_face_correct_offsets.append(is_face_correct_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1:
            is_face_correct_start_offset += 1
        
    df['is_face_correct'] = is_face_correct_list
    df['is_face_correct offset'] = is_face_correct_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'judge' or game == 'lexus2': 
        get_height(binary_data, model_count, is_face_correct_start_offset)
    elif game == 'ogref':
        get_is_invalid(binary_data, model_count, is_face_correct_start_offset)
def get_height(binary_data, model_count, is_face_correct_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 4
    elif game == 'lexus2':
        diff = 1
    height_start_offset = is_face_correct_start_offset + diff
    height_offsets = [height_start_offset]
    height_list = []
    for i in range(0, model_count):
        height = int.from_bytes(binary_data[height_start_offset:height_start_offset+2], 'little')
        height_list.append(height)
        if i != model_count - 1:
            height_start_offset += 2
            height_offsets.append(height_start_offset)
        
    df['height'] = height_list
    df['height offset'] = height_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_height_range(binary_data, model_count, height_start_offset)

def get_height_range(binary_data, model_count, height_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 4
    elif game == 'lexus2':
        diff = 8
    height_range_start_offset = height_start_offset + diff
    height_range_offsets = [height_range_start_offset]
    height_range_list = []
    for i in range(0, model_count):
        height_range = int.from_bytes(binary_data[height_range_start_offset:height_range_start_offset+2], 'little')
        height_range_list.append(height_range)
        if i != model_count - 1:
            height_range_start_offset += 2
            height_range_offsets.append(height_range_start_offset)
        
    df['height_range'] = height_range_list
    df['height_range offset'] = height_range_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_body_type(binary_data, model_count, height_range_start_offset)

def get_body_type(binary_data, model_count, height_range_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 4
    elif game == 'lexus2':
        diff = 8
    body_type_start_offset = height_range_start_offset + diff
    body_type_offsets = [body_type_start_offset]
    body_type_list = []
    for i in range(0, model_count):
        body_type = binary_data[body_type_start_offset]
        body_type_list.append(body_type)
        if i != model_count - 1:
            body_type_start_offset += 1
            body_type_offsets.append(body_type_start_offset)
        
    df['body_type'] = body_type_list
    df['body_type offset'] = body_type_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_language(binary_data, model_count, body_type_start_offset)

def get_language(binary_data, model_count, body_type_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    language_start_offset = body_type_start_offset + diff
    language_offsets = [language_start_offset] 
    language_list = []
    for i in range(0, model_count):
        language = binary_data[language_start_offset]
        language_list.append(language)
        if i != model_count - 1:
            language_start_offset += 1
            language_offsets.append(language_start_offset)
        
    df['language'] = language_list
    df['language offset'] = language_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'judge' or game == 'lexus2':
        get_bag_type(binary_data, model_count, language_start_offset)
    elif game == 'ogref':
        get_voicer(binary_data, model_count, language_start_offset)
def get_voicer(binary_data, model_count, language_start_offset):
    voicer_start_offset = language_start_offset + 2
    voicer_offsets = [voicer_start_offset] 
    voicer_list = []
    for i in range(0, model_count):
        voicer = int.from_bytes(binary_data[voicer_start_offset:voicer_start_offset+2], 'little')
        voicer_list.append(voicer)
        if i != model_count - 1:
            voicer_start_offset += 2
            voicer_offsets.append(voicer_start_offset)
        
    df['voicer'] = voicer_list
    df['voicer offset'] = voicer_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_face_target(binary_data, model_count, voicer_start_offset)

def get_face_target(binary_data, model_count, voicer_start_offset):
    face_target_start_offset = voicer_start_offset + 4
    face_target_offsets = [face_target_start_offset] 
    face_target_list = []
    for i in range(0, model_count):
        face_target = int.from_bytes(binary_data[face_target_start_offset:face_target_start_offset+4], 'little')
        face_target_list.append(face_target)
        if i != model_count - 1:
            face_target_start_offset += 4
            face_target_offsets.append(face_target_start_offset)
        
    df['face_target'] = face_target_list
    df['face_target offset'] = face_target_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_tex_skin(binary_data, model_count, face_target_start_offset)

def get_bag_type(binary_data, model_count, language_start_offset):
    if game == 'judge':
        diff = 2
    elif game == 'lexus2' or game == 'ogref':
        diff = 8
    bag_type_start_offset = language_start_offset + diff
    bag_type_offsets = [bag_type_start_offset]
    bag_type_list = []
    for i in range(0, model_count):
        bag_type = binary_data[bag_type_start_offset]
        bag_type_list.append(bag_type)
        if i != model_count - 1:
            bag_type_start_offset += 1
            bag_type_offsets.append(bag_type_start_offset)
        
    df['bag_type'] = bag_type_list
    df['bag_type offset'] = bag_type_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'judge' or game == 'lexus2':
        get_tex_skin(binary_data, model_count, bag_type_start_offset)
    elif game == 'ogref':
        get_is_face_correct(binary_data, model_count, bag_type_start_offset)

def get_tex_skin(binary_data, model_count, bag_type_start_offset):
    if game == 'judge':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    elif game == 'ogref':
        diff = 4
    tex_skin_start_offset = bag_type_start_offset + diff
    tex_skin_offsets = [tex_skin_start_offset]
    tex_skin_list = []
    for i in range(0, model_count):
        tex_skin = binary_data[tex_skin_start_offset]
        tex_skin_list.append(tex_skin)
        if i != model_count - 1:
            tex_skin_start_offset += 1
            tex_skin_offsets.append(tex_skin_start_offset)
        
    df['tex_skin'] = tex_skin_list
    df['tex_skin offset'] = tex_skin_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_face1(binary_data, model_count, tex_skin_start_offset)

def get_tex_face1(binary_data, model_count, tex_skin_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_face1_start_offset = tex_skin_start_offset + diff
    tex_face1_offsets = [tex_face1_start_offset]
    tex_face1_list = []
    for i in range(0, model_count):
        tex_face1 = binary_data[tex_face1_start_offset]
        tex_face1_list.append(tex_face1)
        if i != model_count - 1:
            tex_face1_start_offset += 1
            tex_face1_offsets.append(tex_face1_start_offset)
        
    df['tex_face1'] = tex_face1_list
    df['tex_face1 offset'] = tex_face1_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_face2(binary_data, model_count, tex_face1_start_offset)

def get_tex_face2(binary_data, model_count, tex_face1_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_face2_start_offset = tex_face1_start_offset + diff
    tex_face2_offsets = [tex_face2_start_offset]
    tex_face2_list = []
    for i in range(0, model_count):
        tex_face2 = binary_data[tex_face2_start_offset]
        tex_face2_list.append(tex_face2)
        if i != model_count - 1:
            tex_face2_start_offset += 1
            tex_face2_offsets.append(tex_face2_start_offset)
        
    df['tex_face2'] = tex_face2_list
    df['tex_face2 offset'] = tex_face2_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_face3(binary_data, model_count, tex_face2_start_offset)

def get_tex_face3(binary_data, model_count, tex_face2_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_face3_start_offset = tex_face2_start_offset + diff
    tex_face3_offsets = [tex_face3_start_offset]
    tex_face3_list = []
    for i in range(0, model_count):
        tex_face3 = binary_data[tex_face3_start_offset]
        tex_face3_list.append(tex_face3)
        if i != model_count - 1:
            tex_face3_start_offset += 1
            tex_face3_offsets.append(tex_face3_start_offset)
        
    df['tex_face3'] = tex_face3_list
    df['tex_face3 offset'] = tex_face3_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_face4(binary_data, model_count, tex_face3_start_offset)

def get_tex_face4(binary_data, model_count, tex_face3_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_face4_start_offset = tex_face3_start_offset + diff
    tex_face4_offsets = [tex_face4_start_offset]
    tex_face4_list = []
    for i in range(0, model_count):
        tex_face4 = binary_data[tex_face4_start_offset]
        tex_face4_list.append(tex_face4)
        if i != model_count - 1:
            tex_face4_start_offset += 1
            tex_face4_offsets.append(tex_face4_start_offset)
        
    df['tex_face4'] = tex_face4_list
    df['tex_face4 offset'] = tex_face4_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_hair1(binary_data, model_count, tex_face4_start_offset)

def get_tex_hair1(binary_data, model_count, tex_face4_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_hair1_start_offset = tex_face4_start_offset + diff
    tex_hair1_offsets = [tex_hair1_start_offset]
    tex_hair1_list = []
    for i in range(0, model_count):
        tex_hair1 = binary_data[tex_hair1_start_offset]
        tex_hair1_list.append(tex_hair1)
        if i != model_count - 1:
            tex_hair1_start_offset += 1
            tex_hair1_offsets.append(tex_hair1_start_offset)
        
    df['tex_hair1'] = tex_hair1_list
    df['tex_hair1 offset'] = tex_hair1_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_hair2(binary_data, model_count, tex_hair1_start_offset)

def get_tex_hair2(binary_data, model_count, tex_hair1_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_hair2_start_offset = tex_hair1_start_offset + diff
    tex_hair2_offsets = [tex_hair2_start_offset]
    tex_hair2_list = []
    for i in range(0, model_count):
        tex_hair2 = binary_data[tex_hair2_start_offset]
        tex_hair2_list.append(tex_hair2)
        if i != model_count - 1:
            tex_hair2_start_offset += 1
            tex_hair2_offsets.append(tex_hair2_start_offset)
        
    df['tex_hair2'] = tex_hair2_list
    df['tex_hair2 offset'] = tex_hair2_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tex_tops1(binary_data, model_count, tex_hair2_start_offset)

def get_tex_tops1(binary_data, model_count, tex_hair2_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_tops1_start_offset = tex_hair2_start_offset + diff
    tex_tops1_offsets = [tex_tops1_start_offset]
    tex_tops1_list = []
    for i in range(0, model_count):
        tex_tops1 = binary_data[tex_tops1_start_offset]
        tex_tops1_list.append(tex_tops1)
        if i != model_count - 1:
            tex_tops1_start_offset += 1
            tex_tops1_offsets.append(tex_tops1_start_offset)
        
    df['tex_tops1'] = tex_tops1_list
    df['tex_tops1 offset'] = tex_tops1_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_tex_tops2(binary_data, model_count, tex_tops1_start_offset)

def get_tex_tops2(binary_data, model_count, tex_tops1_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_tops2_start_offset = tex_tops1_start_offset + diff
    tex_tops2_offsets = [tex_tops2_start_offset]
    tex_tops2_list = []
    for i in range(0, model_count):
        tex_tops2 = binary_data[tex_tops2_start_offset]
        tex_tops2_list.append(tex_tops2)
        if i != model_count - 1:
            tex_tops2_start_offset += 1
            tex_tops2_offsets.append(tex_tops2_start_offset)
        
    df['tex_tops2'] = tex_tops2_list
    df['tex_tops2 offset'] = tex_tops2_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)    
    get_tex_tops3(binary_data, model_count, tex_tops2_start_offset)

def get_tex_tops3(binary_data, model_count, tex_tops2_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_tops3_start_offset = tex_tops2_start_offset + diff
    tex_tops3_offsets = [tex_tops3_start_offset]
    tex_tops3_list = []
    for i in range(0, model_count):
        tex_tops3 = binary_data[tex_tops3_start_offset]
        tex_tops3_list.append(tex_tops3)
        if i != model_count - 1:
            tex_tops3_start_offset += 1
            tex_tops3_offsets.append(tex_tops3_start_offset)
        
    df['tex_tops3'] = tex_tops3_list
    df['tex_tops3 offset'] = tex_tops3_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_tex_tops4(binary_data, model_count, tex_tops3_start_offset)

def get_tex_tops4(binary_data, model_count, tex_tops3_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_tops4_start_offset = tex_tops3_start_offset + diff
    tex_tops4_offsets = [tex_tops4_start_offset]
    tex_tops4_list = []
    for i in range(0, model_count):
        tex_tops4 = binary_data[tex_tops4_start_offset]
        tex_tops4_list.append(tex_tops4)
        if i != model_count - 1:
            tex_tops4_start_offset += 1
            tex_tops4_offsets.append(tex_tops4_start_offset)
        
    df['tex_tops4'] = tex_tops4_list
    df['tex_tops4 offset'] = tex_tops4_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_tex_btms1(binary_data, model_count, tex_tops4_start_offset)

def get_tex_btms1(binary_data, model_count, tex_tops4_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_btms1_start_offset = tex_tops4_start_offset + diff
    tex_btms1_offsets = [tex_btms1_start_offset]
    tex_btms1_list = []
    for i in range(0, model_count):
        tex_btms1 = binary_data[tex_btms1_start_offset]
        tex_btms1_list.append(tex_btms1)
        if i != model_count - 1:
            tex_btms1_start_offset += 1
            tex_btms1_offsets.append(tex_btms1_start_offset)
        
    df['tex_btms1'] = tex_btms1_list
    df['tex_btms1 offset'] = tex_btms1_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_tex_btms2(binary_data, model_count, tex_btms1_start_offset)

def get_tex_btms2(binary_data, model_count, tex_btms1_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_btms2_start_offset = tex_btms1_start_offset + diff
    tex_btms2_offsets = [tex_btms2_start_offset]
    tex_btms2_list = []
    for i in range(0, model_count):
        tex_btms2 = binary_data[tex_btms2_start_offset]
        tex_btms2_list.append(tex_btms2)
        if i != model_count - 1:
            tex_btms2_start_offset += 1
            tex_btms2_offsets.append(tex_btms2_start_offset)
        
    df['tex_btms2'] = tex_btms2_list
    df['tex_btms2 offset'] = tex_btms2_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_tex_btms3(binary_data, model_count, tex_btms2_start_offset)

def get_tex_btms3(binary_data, model_count, tex_btms2_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    
    tex_btms3_start_offset = tex_btms2_start_offset + diff
    tex_btms3_offsets = [tex_btms3_start_offset]
    tex_btms3_list = []
    for i in range(0, model_count):
        tex_btms3 = binary_data[tex_btms3_start_offset]
        tex_btms3_list.append(tex_btms3)
        if i != model_count - 1:
            tex_btms3_start_offset += 1
            tex_btms3_offsets.append(tex_btms3_start_offset)
        
    df['tex_btms3'] = tex_btms3_list
    df['tex_btms3 offset'] = tex_btms3_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_dedit_category(binary_data, model_count, tex_btms3_start_offset)

def get_dedit_category(binary_data, model_count, tex_btms3_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    dedit_category_start_offset = tex_btms3_start_offset + diff
    dedit_category_offsets = [dedit_category_start_offset]
    dedit_category_list = []
    for i in range(0, model_count):
        dedit_category = binary_data[dedit_category_start_offset]
        dedit_category_list.append(dedit_category)
        if i != model_count - 1:
            dedit_category_start_offset += 1
            dedit_category_offsets.append(dedit_category_start_offset)
        
    df['dedit_category'] = dedit_category_list
    df['dedit_category offset'] = dedit_category_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_dedit(binary_data, model_count, dedit_category_start_offset)

def get_dedit(binary_data, model_count, dedit_category_start_offset):
    if game == 'judge' or game == 'ogref':
        diff = 2
    elif game == 'lexus2':
        diff = 8
    dedit_start_offset = dedit_category_start_offset + diff
    dedit_offsets = [dedit_start_offset]
    dedit_list = []
    for i in range(0, model_count):
        if game == 'judge':
            dedit = int.from_bytes(binary_data[dedit_start_offset:dedit_start_offset+4], 'little')
        elif game == 'lexus2' or game == 'ogref':
            dedit = int.from_bytes(binary_data[dedit_start_offset:dedit_start_offset+2], 'little')
        dedit_list.append(dedit)
        if i != model_count - 1:
            if game == 'judge':
                dedit_start_offset += 4
            elif game == 'lexus2' or game == 'ogref':
                dedit_start_offset += 2
            dedit_offsets.append(dedit_start_offset)
        
    df['dedit'] = dedit_list
    df['dedit offset'] = dedit_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_face(binary_data, model_count, dedit_start_offset)

def get_face(binary_data, model_count, dedit_start_offset):
    if game == 'judge' or game == 'lexus2':
        diff = 8
    elif game == 'ogref':
        diff = 4
    face_start_offset = dedit_start_offset + diff
    face_offsets = [face_start_offset]
    face_list = []
    for i in range(0, model_count):
        face = int.from_bytes(binary_data[face_start_offset:face_start_offset+4], 'little')
        face_list.append(face)
        if i != model_count - 1:
            face_start_offset += 4
            face_offsets.append(face_start_offset)
        
    df['face'] = face_list
    df['face offset'] = face_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_hair(binary_data, model_count, face_start_offset)

def get_hair(binary_data, model_count, face_start_offset):
    if game == 'judge' or game == 'lexus2':
        diff = 8
    elif game == 'ogref':
        diff = 4
    hair_start_offset = face_start_offset + diff
    hair_offsets = [hair_start_offset]
    hair_list = []
    for i in range(0, model_count):
        hair = int.from_bytes(binary_data[hair_start_offset:hair_start_offset+4], 'little')
        hair_list.append(hair)
        if i != model_count - 1:
            hair_start_offset += 4
            hair_offsets.append(hair_start_offset)
        
    df['hair'] = hair_list
    df['hair offset'] = hair_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_tops(binary_data, model_count, hair_start_offset)  

def get_tops(binary_data, model_count, hair_start_offset):
    if game == 'judge' or game == 'lexus2':
        diff = 8
    elif game == 'ogref':
        diff = 4
    tops_start_offset = hair_start_offset + diff
    tops_offsets = [tops_start_offset]
    tops_list = []
    for i in range(0, model_count):
        tops = int.from_bytes(binary_data[tops_start_offset:tops_start_offset+4], 'little')
        tops_list.append(tops)
        if i != model_count - 1:
            tops_start_offset += 4
            tops_offsets.append(tops_start_offset)
        
    df['tops'] = tops_list
    df['tops offset'] = tops_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_btms(binary_data, model_count, tops_start_offset)

def get_btms(binary_data, model_count, tops_start_offset):
    if game == 'judge' or game == 'lexus2':
        diff = 8
    elif game == 'ogref':
        diff = 4
    btms_start_offset = tops_start_offset + diff
    btms_offsets = [btms_start_offset]
    btms_list = []
    for i in range(0, model_count):
        btms = int.from_bytes(binary_data[btms_start_offset:btms_start_offset+4], 'little')
        btms_list.append(btms)
        if i != model_count - 1:
            btms_start_offset += 4
            btms_offsets.append(btms_start_offset)
        
    df['btms'] = btms_list
    df['btms offset'] = btms_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_face_flags(binary_data, model_count, btms_start_offset)

def get_face_flags(binary_data, model_count, btms_start_offset):
    if game == 'judge' or game == 'lexus2':
        diff = 8
    elif game == 'ogref':
        diff = 4
    face_flags_start_offset = btms_start_offset + diff
    face_flags_offsets = [face_flags_start_offset]
    face_flags_list = []
    for i in range(0, model_count):
        face_flags = int.from_bytes(binary_data[face_flags_start_offset:face_flags_start_offset+8], 'little')
        face_flags_list.append(face_flags)
        if i != model_count - 1:
            face_flags_start_offset += 8
            face_flags_offsets.append(face_flags_start_offset)
        
    df['face_flags'] = face_flags_list
    df['face_flags offset'] = face_flags_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)  
    get_hair_flags(binary_data, model_count, face_flags_start_offset)

def get_hair_flags(binary_data, model_count, face_flags_start_offset):
    diff = 8
    hair_flags_start_offset = face_flags_start_offset + diff
    hair_flags_offsets = [hair_flags_start_offset]
    hair_flags_list = []
    for i in range(0, model_count):
        hair_flags = int.from_bytes(binary_data[hair_flags_start_offset:hair_flags_start_offset+8], 'little')
        hair_flags_list.append(hair_flags)
        if i != model_count - 1:
            hair_flags_start_offset += 8
            hair_flags_offsets.append(hair_flags_start_offset)
        
    df['hair_flags'] = hair_flags_list
    df['hair_flags offset'] = hair_flags_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_tops_flags(binary_data, model_count, hair_flags_start_offset)

def get_tops_flags(binary_data, model_count, hair_flags_start_offset):
    diff = 8
    tops_flags_start_offset = hair_flags_start_offset + diff
    tops_flags_offsets = [tops_flags_start_offset]
    tops_flags_list = []
    for i in range(0, model_count):
        tops_flags = int.from_bytes(binary_data[tops_flags_start_offset:tops_flags_start_offset+8], 'little')
        tops_flags_list.append(tops_flags)
        if i != model_count - 1:
            tops_flags_start_offset += 8
            tops_flags_offsets.append(tops_flags_start_offset)
        
    df['tops_flags'] = tops_flags_list
    df['tops_flags offset'] = tops_flags_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_btms_flags(binary_data, model_count, tops_flags_start_offset)

def get_btms_flags(binary_data, model_count, tops_flags_start_offset):
    diff = 8
    btms_flags_start_offset = tops_flags_start_offset + diff
    btms_flags_offsets = [btms_flags_start_offset]
    btms_flags_list = []
    for i in range(0, model_count):
        btms_flags = int.from_bytes(binary_data[btms_flags_start_offset:btms_flags_start_offset+8], 'little')
        btms_flags_list.append(btms_flags)
        if i != model_count - 1:
            btms_flags_start_offset += 8
            btms_flags_offsets.append(btms_flags_start_offset)
        
    df['btms_flags'] = btms_flags_list
    df['btms_flags offset'] = btms_flags_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'judge' or game == 'lexus2': 
        get_cloth_physics(binary_data, model_count, btms_flags_start_offset)
    elif game == 'ogref':
        get_bag_type(binary_data, model_count, btms_flags_start_offset)

def get_cloth_physics(binary_data, model_count, btms_flags_start_offset):
    cloth_physics_start_offset = btms_flags_start_offset + 8
    cloth_physics_offsets = []
    cloth_physics_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        cloth_physics = list(f'{binary_data[cloth_physics_start_offset]:0>8b}')
        cloth_physics.reverse()
        for data in cloth_physics:
            if (model_iterator == model_count):
                break
            else:  
                cloth_physics_list.append(data)
                cloth_physics_offsets.append(cloth_physics_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1:
            cloth_physics_start_offset += 1
        
    df['cloth_physics'] = cloth_physics_list
    df['cloth_physics offset'] = cloth_physics_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_shoes_kind(binary_data, model_count, cloth_physics_start_offset)

def get_shoes_kind(binary_data, model_count, cloth_physics_start_offset):
    if game == 'judge':
        diff = 4
    elif game == 'lexus2' or game == 'ogref':
        diff = 1
    shoes_kind_start_offset = cloth_physics_start_offset + diff
    shoes_kind_offsets = [shoes_kind_start_offset]
    shoes_kind_list = []
    for i in range(0, model_count):
        shoes_kind = binary_data[shoes_kind_start_offset]
        shoes_kind_list.append(shoes_kind)
        if i != model_count - 1:
            shoes_kind_start_offset += 1
            shoes_kind_offsets.append(shoes_kind_start_offset)
        
    df['shoes_kind'] = shoes_kind_list
    df['shoes_kind offset'] = shoes_kind_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_auto_wrinkle_scale(binary_data, model_count, shoes_kind_start_offset)

def get_auto_wrinkle_scale(binary_data, model_count, shoes_kind_start_offset):
    if game == 'judge':
        diff = 2
    elif game == 'lexus2' or game == 'ogref':
        diff = 8
    auto_wrinkle_scale_start_offset = shoes_kind_start_offset + diff
    auto_wrinkle_scale_offsets = [auto_wrinkle_scale_start_offset]
    auto_wrinkle_scale_list = []
    for i in range(0, model_count):
        auto_wrinkle_scale = struct.unpack('<f', binary_data[auto_wrinkle_scale_start_offset:auto_wrinkle_scale_start_offset+4])
        auto_wrinkle_scale_list.append(auto_wrinkle_scale[0])
        if i != model_count - 1:
            auto_wrinkle_scale_start_offset += 4
            auto_wrinkle_scale_offsets.append(auto_wrinkle_scale_start_offset)
        
    df['auto_wrinke_scale'] = auto_wrinkle_scale_list
    df['auto_wrinkle_scale offset'] = auto_wrinkle_scale_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    if game == 'judge':
        get_can_sit(binary_data, model_count, auto_wrinkle_scale_start_offset)

def get_can_sit(binary_data, model_count, auto_wrinkle_scale_start_offset):
    can_sit_start_offset = auto_wrinkle_scale_start_offset + 8
    can_sit_offsets = []
    can_sit_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        can_sit = list(f'{binary_data[can_sit_start_offset]:0>8b}')
        can_sit.reverse()
        for data in can_sit:
            if (model_iterator == model_count):
                break
            else:  
                can_sit_list.append(data)
                can_sit_offsets.append(can_sit_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1: 
            can_sit_start_offset += 1
        
    df['can_sit'] = can_sit_list
    df['can_sit offset'] = can_sit_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_is_use_fur(binary_data, model_count, can_sit_start_offset)

def get_is_use_fur(binary_data, model_count, can_sit_start_offset):
    is_use_fur_start_offset = can_sit_start_offset + 4
    is_use_fur_offsets = []
    is_use_fur_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        is_use_fur = list(f'{binary_data[is_use_fur_start_offset]:0>8b}')
        is_use_fur.reverse()
        for data in is_use_fur:
            if (model_iterator == model_count):
                break
            else:  
                is_use_fur_list.append(data)
                is_use_fur_offsets.append(is_use_fur_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1:
            is_use_fur_start_offset += 1
        
    df['is_use_fur'] = is_use_fur_list
    df['is_use_fur offset'] = is_use_fur_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)

def get_is_invalid(binary_data, model_count, is_face_correct_start_offset):
    is_invalid_start_offset = is_face_correct_start_offset + 4
    is_invalid_offsets = []
    is_invalid_list = []
    model_iterator = 0
    for i in range (0, math.ceil(model_count / 8)):
        is_invalid = list(f'{binary_data[is_invalid_start_offset]:0>8b}')
        is_invalid.reverse()
        for data in is_invalid:
            if (model_iterator == model_count):
                break
            else:  
                is_invalid_list.append(data)
                is_invalid_offsets.append(is_invalid_start_offset)
                model_iterator += 1
        if i != math.ceil(model_count / 8) - 1:
            is_invalid_start_offset += 1
        
    df['is_invalid'] = is_invalid_list
    df['is_invalid offset'] = is_invalid_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False)
    get_org_id(binary_data, model_count, is_invalid_start_offset)

def get_org_id(binary_data, model_count, is_invalid_start_offset): 
    org_id_start_offset = is_invalid_start_offset + 4
    org_id_offsets = [org_id_start_offset]
    org_id_list = []
    for i in range(0, model_count):
        org_id = int.from_bytes(binary_data[org_id_start_offset:org_id_start_offset+2], 'little')
        org_id_list.append(org_id)
        if i != model_count - 1:
            org_id_start_offset += 2
            org_id_offsets.append(org_id_start_offset)
        
    df['org_id'] = org_id_list
    df['org_id offset'] = org_id_offsets
    df.to_csv('modeldata_' + game + '.csv',sep=';', index=False) 
    get_is_reuse(binary_data, model_count, org_id_start_offset)
get_model_names(binary_data, model_count)
print('file saved')