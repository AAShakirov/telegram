import requests
from config import API_link

updates = requests.get(f'{API_link}/getUpdates?offset=-1').json()

message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']
sent_message = requests.get(f'{API_link}/sendMessage?chat_id={chat_id}&text=Ты написал: {text}')