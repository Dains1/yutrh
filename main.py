from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from kebord.keyboards import (get_keybord_1, get_keybord_2)
from kebord.key_inline import get_keybord_inlain, get_keybord_inlain_2, get_keybord_inlain_3, get_keybord_inlain_4
import random
from datetime import datetime
from database.database import initialize_db, add_user, get_user

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для получения информации'),
        types.BotCommand(command='/kick', description='Команда для кика участника бота'),
        types.BotCommand(command='/mute', description='Команда для мута участника'),
        types.BotCommand(command='/unmute', description='Команда для размута участника')
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if not user:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        text = 'Привет! Я рад видеть нового пользователя.'
    else:
        text = 'Привет! Рад тебя видеть снова.'

    await message.answer(text, reply_markup=get_keybord_1())
    await message.answer('Ты на клавеатуре 1', reply_markup=get_keybord_inlain_3())






@dp.callback_query_handler(lambda c: c.data == 'send_random')
async def send_random(callback_query: types.CallbackQuery):
    random_nam =random.randint(1,100)
    await callback_query.message.answer(f'Случяйное число: {random_nam}')

@dp.callback_query_handler(lambda c: c.data == 'send_detetime')
async def send_detetime(callback_query: types.CallbackQuery):
    curent_time = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.edit_text(f'Текущие время {curent_time}',)

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты на клавеатуре 2', reply_markup= get_keybord_inlain_4())


@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты на клавеатуре 1', reply_markup= get_keybord_inlain_3())

@dp.message_handler(lambda message: message.text == 'Отправь фото мяу мяу')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?pos=0&from=tabbar&img_url=http%3A%2F%2Fgas-kvas.com%2Fgrafic%2Fuploads%2Fposts%2F2023-09%2F1695931383_gas-kvas-com-p-kartinki-s-kotami-9.jpg&text=%D0%BA%D0%BE%D1%82&rpt=simage&lr=213', caption= 'Еды дай', reply_markup= get_keybord_inlain())

@dp.message_handler(lambda message: message.text == 'Переход на другую клавеатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут пёсик', reply_markup= get_keybord_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото тяф тяф')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://yandex.ru/images/search?text=%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0+vbkfz+&pos=17&rpt=simage&img_url=https%3A%2F%2Fpoliteka.net%2Fimages%2F2016%2F07%2F14%2FYphvRUNANCDFsrMVdZkyNKgclPFfTwj0.jpg&from=tabbar&lr=213', caption= 'тяф тяф', reply_markup= get_keybord_inlain_2())

@dp.message_handler(lambda message: message.text == 'Переход обратно')
async def button_4_click(message: types.Message):
    await message.answer('Тут кот', reply_markup= get_keybord_1())


@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.answer('Ты на клавеатуре 1')

@dp.message_handler(commands= 'kik')
async def kik(message: types.Message):
    await message.reply('Минус 1 не очень умный пользователь')

@dp.message_handler(commands= 'mute')
async def mute(message: types.Message):
    await message.reply('Помалчи пока сладенький')

@dp.message_handler(commands= 'unmute')
async def unmute(message: types.Message):
    await message.reply('Эх а так харашо было... в тишене')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)