from telethon.sync import TelegramClient
 
import csv
import json

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 0
api_hash = ''
phone = ''
 
end = "true"
client = TelegramClient(phone, api_id, api_hash)

client.start()

chats = []
last_date = None
size_chats = 200
groups=[]

result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=size_chats,
            hash = 0
        ))
chats.extend(result.chats)

for chat in chats:
    groups.append(chat)
while(end != "Exit"):
    print('Выберите номер группы из перечня:')
    i=0
    group_name = ""
    for g in groups:
        print(str(i) + '- ' + g.title)
        i+=1

    g_index = input("Введите нужную цифру: ")
    target_group=groups[int(g_index)]
    print('Узнаём пользователей...')

    group_name = target_group.title

    all_participants = []
    items = []
    all_participants = client.iter_dialogs
    index = 0

    all_participants = client.get_messages(target_group)
    for x in all_participants:  # show the 10 messages
        latest_news = x.id

    while(index < 10):
        all_participants = client.get_messages(target_group, ids=latest_news-index)
        try:
            if(str(all_participants.message) != ""):
                items.append({'id_message': str(all_participants.id), 'message': str(all_participants.message), 'date_message': str(all_participants.date), "source": group_name})
            index = index + 1
        except:
            print("Attribute Error id_message: " + all_participants.id)

    with open('news.json', 'a', encoding='utf-8') as outfile:
        json.dump(items ,outfile, ensure_ascii=False)
    
    end = input("Выйти? <Exit>")
