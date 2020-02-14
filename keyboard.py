import json

keyboard = {

    "one_time": True,
    "inline": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "узнать домашку"
            }
        }],

        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "поржать"
            },
            "color": "positive"
        }]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))