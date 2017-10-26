from . import interfaces

def bot_controller(request):
    reply_text = ""

    for e in request["events"]:
        reply_token = e["replyToken"]

        if e["type"] == "message":

            if e["message"]["type"] == "text":
                
                payload += create_reply_text(e)
            #else:
                #payload +=
            payload.update({"replyToken":reply_token})
            return payload







# there no each other
def create_reply_text(request):
    
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

