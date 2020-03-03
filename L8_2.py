import requests, json

userId = '小佛'
apikey = str('1475eed9809044c78dab2a9dbe297755')

def robot(content):
    api = 'http://openapi.tuling123.com/openapi/api/v2'

    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": content
            },
        "userInfo": {
            "apiKey": apikey,
            "userId": userId
            }
        }
    }

    jsondata = json.dumps(data)
    res = requests.post(api, data=jsondata)
    res.encoding = 'utf-8'
    rebot_json = json.loads(res.content)
    print(rebot_json['results'][0]['values']['text'])

# for x in range(10):
#     content = input("talk:")
#     robot(content)
#     if x == 10:
#         break

# while True:
#     content = input("talk:")
#     if content == 'bye':
#         break

while True:
    content = input("talk:")
    robot(content)
