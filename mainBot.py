# работа над второй кнопкой
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from config import TOKEN
from enter_to_db import *
import sqlite3
import asyncio
import datetime
from telethon import functions
# TelegramClient
from telethon import functions
from telethon import utils
import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel
from enter_to_db import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
con = sqlite3.connect('sqlite_python.db')

#################################################
async def start_client(delay):
    x = 1
    db = sqlite3.connect('all_db/Account.db')
    cur = db.cursor()
    cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone, ' Номер ', x)
    cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_hash = str(cur.fetchone()[0])
    session = str("anon" + str(x))
    client = TelegramClient(session, api_id, api_hash)
    task1 = asyncio.create_task(client.start())
    await asyncio.sleep(delay)
    return await task1

async def get_chat_name_on_url(delay,url):
    x = 1
    db = sqlite3.connect('all_db/Account.db')
    cur = db.cursor()
    cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone, ' Номер ', x)
    cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_hash = str(cur.fetchone()[0])
    session = str("anon" + str(x))
    client = TelegramClient(session, api_id, api_hash)
    task1 = asyncio.create_task(client.start())
    await asyncio.sleep(delay)
    print("client Start")
    await task1
    # NAME CHAT
    channel_full_info = await client(GetFullChannelRequest(url))
    chat_id = channel_full_info.full_chat.id
    chanPeer = PeerChannel(channel_id=chat_id)
    channel_entity = await client.get_entity(chanPeer)
    print("NAME>>>>>", channel_entity.title)
    name_chat = channel_entity.title
    disconnect = asyncio.create_task(client.disconnect())
    await disconnect
    return name_chat

# Взятие URL с DB и поиск текущего имени чата и запись имени чата в DB.
async def get_chat_current_name():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    client=start_client(1)
    #print(db)
    for i in db:
        print(i[1])
        time.sleep(1)
        channel = i[1]
        full = client(functions.channels.GetFullChannelRequest(channel))
        full_channel = full.full_chat
        channel_full_info = client(GetFullChannelRequest(channel=channel))
        #print(channel_full_info.full_chat.about)
        #print(full_channel.migrated_from_chat_id)
        chat_id = channel_full_info.full_chat.id
        chanPeer = PeerChannel(channel_id=chat_id)
        channel_entity = client.get_entity(chanPeer)
        print(channel_entity.title)
        # Запись в базу сначала получаем id а потом по id записываем имя чата
        print(sql_select_id(con,i[1]))
        set = ("original_channel_name")
        set_name = (channel_entity.title)
        where = ('UID')
        where_name = sql_select_id(con,i[1])
        sql_update(con,set,set_name,where,where_name)

# получения  списка ID для автообнавления
async def getID():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    lens=[]
    for i in db:
        #print(i[0])
        lens.append(i[0])
        #sql_select_id(con, i[1])
        #print(sql_select_id(con, i[1]))
    return lens

async def getURL():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    lens=[]
    for i in db:
        #print(i[0])
        lens.append(i[1])
        #sql_select_id(con, i[1])
        #print(sql_select_id(con, i[1]))
    return lens

# Получить всех пользователей чата
async def get_all_users(delay,channel):
    print("get_all_users :",channel)
    x = 1
    db = sqlite3.connect('all_db/Account.db')
    cur = db.cursor()
    cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone, ' Номер ', x)
    cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_hash = str(cur.fetchone()[0])
    session = str("anon" + str(x))
    client = TelegramClient(session, api_id, api_hash)
    task1 = asyncio.create_task(client.start())
    await asyncio.sleep(delay)
    print("client Start")
    await task1
    task2 = asyncio.create_task(client.connect())
    await task2

    channel_connect =  await client.get_entity(channel)
    channel_full_info =  await client(GetFullChannelRequest(channel=channel_connect))
    print(channel_full_info.full_chat.participants_count)
    #print(channel_full_info)
    task3 = asyncio.create_task(client.disconnect())
    await task3
    #client.run_until_disconnected()
    return channel_full_info.full_chat.participants_count

# Запись количества пользователей чата в Базу

async def save_len_users(len_users,id,sets):
    if sets ==True:
        set = ("Current_number_of_users_in_channel")
    else:
        set=("number_of_users_at_the_moment_of_insertion_into_the_bot")
    set_name = (str(len_users))
    where = ('UID')
    where_name = str(id)
    print("con,set,set_name,where,where_name >>",con,set,set_name,where,where_name)
    sql_update(con,set,set_name,where,where_name)

async def save_name_chat(name_cha,id,sets):
    if sets ==True:
        set = ("original_channel_name ")
    else:
        set=("previous_channel_names")
    set_name = (str(name_cha))
    where = ('UID')
    where_name = str(id)
    print("save_name_chat !!!")
    sql_update(con,set,set_name,where,where_name)

# Автообновления параметров
async def auto_updates_save_len_users(delay):
    urls = getURL()
    for url in await urls:
        print("Авто обновления >>> ",url)
        #time.sleep(1)
        #print(get_all_users(url))
        #lenuser =get_all_users(url)
        print(sql_select_id(con,url))
        sets=True
        # Получения количества пользователей в группе
        task1 = asyncio.create_task(get_all_users(1, str(url)))
        id = sql_select_id(con, url)
        # Запись количества пользователей чата в Базу
        task2 = asyncio.create_task(save_len_users(await task1, id, sets))
        await task2
        # Запись имени чата в Базу
        task3 = asyncio.create_task(get_chat_name_on_url(5, url))
        # await task3
        sets = False
        task4 = asyncio.create_task(save_name_chat(await task3, id, sets))
        await task4
        await asyncio.sleep(delay)
#asyncio.run(Auto_updates_save_len_users(5))

###################################################################################################################################################

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Main menu"]
    keyboard.add(*buttons)
    await message.reply("HI", reply_markup=keyboard)


####################################################################################
# Главное меню
@dp.message_handler(Text(equals="Main menu"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["First button", "Second button"]
    keyboard.add(*buttons)
    await message.reply("Select mode", reply_markup=keyboard)


@dp.message_handler(Text(equals="First button"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["+ button", "- button", "Main menu"]
    keyboard.add(*buttons)
    await message.reply("Select mode", reply_markup=keyboard)

# Кнопка удаления канала
@dp.message_handler(Text(equals="- button"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Delete channel", "Main menu"]
    keyboard.add(*buttons)

    # Запись во временый файл
    @dp.message_handler()
    async def echo_message(msg: types.Message):
        print(msg.text)
        file = open("temp.txt", "w")
        file.write(msg.text)
        file.close()

    await message.reply("Specify titles ONLY url", reply_markup=keyboard)

# подтверждения удаления канала
@dp.message_handler(Text(equals="Delete channel"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Main menu"]
    keyboard.add(*buttons)
    f = open('temp.txt', 'r')
    con = sqlite3.connect('sqlite_python.db')
    fstr = ''.join(f.read())
    print(fstr)
    temp = (fstr,)
    sql_del(con,temp)
    print("Канал удален: ",temp)
    await message.reply("Select mode", reply_markup=keyboard)

# Добавления канала
@dp.message_handler(Text(equals="+ button"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Save",  "Main menu"]
    keyboard.add(*buttons)

    #Запись во временый файл
    @dp.message_handler()
    async def echo_message(msg: types.Message):
        print(msg.text)
        file = open("temp.txt", "w")
        file.write(msg.text)
        file.close()
    await message.reply("Specify titles via @ or url", reply_markup=keyboard)

# Сохранения канала
@dp.message_handler(Text(equals="Save"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Main menu"]
    keyboard.add(*buttons)
    print('NAME CHANNEL: ')
    f = open('temp.txt', 'r')
    con = sqlite3.connect('sqlite_python.db')
    fstr=''.join(f.read())
    print(fstr)
    temp=(fstr,)
    sql_insert_one(con,temp)

    # Получения количества пользователей в группе
    task1 = asyncio.create_task(get_all_users(1,str(temp[0])))
    id = sql_select_id(con, temp)
    sets=False
    # Запись количества пользователей чата в Базу
    task2 = asyncio.create_task(save_len_users(await task1, id, sets))
    await task2

    # Запись имени чата в Базу
    print("temp[0]",temp[0])
    task3 =asyncio.create_task(get_chat_name_on_url(5,temp[0]))
    #await task3
    sets=True
    task4 = asyncio.create_task(save_name_chat(await task3, id, sets))
    await task4
    # Запись время добавления  чата в Базу
    set = ("Date_of_submission_to_bot")
    set_name = (str(datetime.datetime.now()))
    where = ('UID')
    where_name = str(id)
    print("Date_of_submission_to_bot !!!")
    sql_update(con, set, set_name, where, where_name)
    #количество   изменений изображения чата ( в падло переделывать при создании базы ) костыль но он работает
    set = ("How_many_times")
    set_name = (str(0))
    where = ('UID')
    where_name = str(id)
    print("save_photo_chat !!!")
    sql_update(con, set, set_name, where, where_name)
    await message.reply("Channel added", reply_markup=keyboard)


####################################################################################
buttons = []
urls = []
@dp.message_handler(Text(equals="Second button"))
async def with_puree(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Channel history all", callback_data="Channel_History"))
    buttons_clear()
    await message.answer(" Channel History ", reply_markup=keyboard)


def get_keyboard():
    # Генерация клавиатуры.
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    #urls = []
    for i in db:
        #print(i[2])
        urls.append(i[1])
        buttons.append(types.InlineKeyboardButton(text=str(i[2]), callback_data=str(len(buttons))),)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    #print(len(buttons))
    return keyboard
def buttons_clear():
    buttons.clear()
    urls.clear()
    #print("buttons >>> ",buttons)

@dp.callback_query_handler(text=({ i for i in range(99) }))
async def send_all_chanel(call: types.CallbackQuery):
    print("call: types.CallbackQuery >>>",call.values["data"])
    key = call.values["data"]
    print(key)
    print(urls[int(key)])
    ids = sql_select_id(con,urls[int(key)])

    picture_changed="NO"
    pich = sql_select_How_many_times(con,str(ids))
    if int(pich)!=1:
        picture_changed="YES"

    texts = 'Original channel name ' + sql_select_original_channel_name(con,
                                                                        str(ids)) + '\nPrevious channel name ' + sql_select_previous_channel_names(
        con, str(ids)) + '\nDate of submission to the bot ' + sql_select_Date_of_submission_to_bot(con,
                                                                                                    str(ids)) + '\nHas a picture changed:  ' + picture_changed + '\nHow many times: ' + sql_select_How_many_times(
        con, str(ids)) + "\nCurrent number of users in the channel: " + sql_select_Current_number_of_users_in_channel(
        con,
        str(ids)) + '\nNumber of users at the moment of insertion into the bot: ' + sql_select_number_of_users_at_the_moment_of_insertion_into_the_bot(
        con, str(ids))
    print(texts)

    buttons_clear()
    await call.message.answer(texts, reply_markup=get_keyboard())

@dp.callback_query_handler(text="Channel_History")
async def send_all_chanel(call: types.CallbackQuery):
    await call.message.answer("Channel History",reply_markup=get_keyboard())

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


if __name__ == '__main__':
    executor.start_polling(dp)