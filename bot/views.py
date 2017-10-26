from interface import callback_line

def bot_controller(request):
    reply = ""
    for e in request["events"]:
        reply_token = e["replyToken"]
        if e["type"] == "message":
            if e["message"]["type"] == "text":
                reply += "developing with docomoAPI"
            else:
                reply += "only text message"
            reply_message(reply_token, reply)


def reply_message(reply_token, reply):
    payload = {
        "replyToken":reply_token,
        "messages":[
            {
                "type":"text",
                "text": reply
            }
        ]
    }
    reply_line(payload)
