import os
import json
import requests
from . import views.bot_controller

LINE_REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
LINE_HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + LINE_ACCESS_TOKEN
}

def callback_line(request):
    bot_controller(json.loads(request.body.decode('utf-8')))

def reply_line(reply):
    requests.post(LINE_REPLY_ENDPOINT, headers=LINE_HEADER, data=json.dumps(reply))

