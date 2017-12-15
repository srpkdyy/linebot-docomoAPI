import os
import json
import random
import requests

from . import docomo
from django.shortcuts import render
from django.http import HttpResponse

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}
USER_INFO = 'https://api.line.me/v2/bot/profile/'

def index(request):
    return HttpResponse("It works!")

def callback(request_json):
    reply = ""
    request = parse_json(request_json)
    for e in request["events"]:
        reply_token = e["replyToken"]
        if e["type"] == "message":
            if e["message"]["type"] == "text":
                reply += docomo.reply(e["message"]["text"], get_username(e["source"]["userId"]))
            else:
                reply += "Not text message yet."
            reply_message(reply_token, reply)

def parse_json(request_json):
    return json.loads(request_json.body.decode('utf-8'))

def get_username(request):
    res_json = requests.get(USER_INFO + request, headers=HEADER)
#    res = parse_json(res_json)
#    return res_json["displayName"]
    return res_json.text

def reply_message(reply_token, reply):
    reply_body = {
        "replyToken":reply_token,
        "messages":[
            {
                "type":"text",
                "text": reply
            }
        ]
    }
    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(reply_body))
