from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keybord_inlain():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть котиков', url='https://pixabay.com/ru/photos/search/%d0%ba%d0%be%d1%88%d0%ba%d0%b0/')
    but_inline_2 = InlineKeyboardButton('Посмотреть котят', url='https://pixabay.com/ru/photos/search/%d0%ba%d0%be%d1%82%d0%b5%d0%bd%d0%be%d0%ba/')
    keyboard_inline.add(but_inline, but_inline_2)
    return keyboard_inline

def get_keybord_inlain_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
    but_inline_3 = InlineKeyboardButton('Посмотреть собак', url='https://pixabay.com/ru/photos/search/%d1%81%d0%be%d0%b1%d0%b2%d0%ba%d0%b0/')
    but_inline_4 = InlineKeyboardButton('Посмотреть щенков', url='https://pixabay.com/ru/photos/search/%d1%89%d0%b5%d0%bd%d0%be%d0%ba/')
    keyboard_inline_2.add(but_inline_3, but_inline_4)
    return keyboard_inline_2

def get_keybord_inlain_3():
    keyboard_inline_3 = InlineKeyboardMarkup(row_width=1)
    but_inline_5 = InlineKeyboardButton('Переключится клава 2', callback_data= 'go_to_2')
    but_inline_6 = InlineKeyboardButton('Случайное число', callback_data= 'send_random')
    keyboard_inline_3.add(but_inline_5, but_inline_6)
    return keyboard_inline_3

def get_keybord_inlain_4():
    keyboard_inline_4 = InlineKeyboardMarkup(row_width=1)
    but_inline_7 = InlineKeyboardButton('Переключится клава 1',callback_data= 'go_to_1')
    but_inline_8 = InlineKeyboardButton('Текущие время ',callback_data= 'send_detetime')
    keyboard_inline_4.add(but_inline_7, but_inline_8)
    return keyboard_inline_4