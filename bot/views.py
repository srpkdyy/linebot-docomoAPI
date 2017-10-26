from . import interface

def bot_controller(request):
    reply_text = ""

    for e in request["events"]:
        reply_token = e["replyToken"]

        if e["type"] == "message":
            if e["message"]["type"] == "text":
                reply_text += "developing with docomoAPI"
            else:
                reply_text += "only text message"
            
            return create_reply(reply_token, reply_text)


def create_reply(reply_token, reply_text):
    payload = {
        "replyToken":reply_token,
        "messages":[
            {
                "type":"text",
                "text": reply_text
            }
        ]
    }
    return payload
