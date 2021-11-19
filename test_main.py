
from telethon import functions
from telethon import utils
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest,GetParticipantsRequest
from telethon.tl.types import PeerChannel,InputChannel
import time
from config import ADMIN



from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.functions.channels import GetParticipantsRequest

from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser


import sqlite3
from enter_to_db import *

con = sqlite3.connect('sqlite_python.db')

admin=ADMIN

# The first account is used by a bot. use accounts only from the second !
x =1
max_accounts=12
#  TIME UPDATE
hour = 9
min =59
# delay time when changing accounts
changing_accounts = 60 # seconds


h = time.strftime("%H")
m = time.strftime("%M")
db = sqlite3.connect('Account.db')
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
client.start()
client.connect()


#urls =client.get_participants(str("https://t.me/viktortanchikchannel"))



channel_connect = client(ResolveUsernameRequest('zernomart')) # Your channel username

user = client(ResolveUsernameRequest('zernomart')) # Your channel admin username
print(user)
#admins = [InputUserSelf(), InputUser(user.users[0].id, user.users[0].access_hash)] # admins
#admins = [] # No need admins for join and leave and invite filters

filter = None # All events
filter = ChannelAdminLogEventsFilter(True, False, False, False, True, True, True, True, True, True, True, True, True, True)
cont = 0
list = [0,100,200,300]
i=0
for num in list:
    result = client(GetParticipantsRequest(InputChannel(channel_connect.chats[0].id, channel_connect.chats[0].access_hash), filter, num, 100, 0))
    for _user in result.users:
        print( str(_user.id) + ';' + str(_user.username) + ';' + str(_user.first_name) + ';' + str(_user.last_name) )
        i+=1
print(i)
#with open(''.join(['users/', str(_user.id)]), 'w') as f: f.write(str(_user.id))


#"https://t.me/channkt"
def chanelname(url,):
    print(url)
    channel_connect = client.get_entity(url)
    channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
    #result = client(GetParticipantsRequest(InputChannel(channel_connect.chats[0].id, channel_connect.chats[0].access_hash), filter, num, 100, 0))
    # print(channel_full_info.full_chat.participants_count)
    #print(channel_full_info.chats)
    #print("##########")
    print("channel name >> ",channel_full_info.chats[0].title)
    return channel_full_info.chats[0].title
#url="https://t.me/Pipl_test_chat"
#url='https://t.me/channkt'
url='https://t.me/perepichka_news'
#chanelname(url)