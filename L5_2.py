import requests, bs4

url = 'https://www.kuaidi100.com/'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie':
    'csrftoken=WxlTM1AGpITnXam8KqlkvFEN6jLuNNKZOctEQ8mxjzM; WWWID=WWW633095FA395B4A10A82585192F6F001A; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1582521935; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1582521935',
    'Host': 'www.kuaidi100.com',
    'Referer': 'https://www.kuaidi100.com/',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

params = {
    }

res = requests.get(url, headers = headers)
kd_json = res.json()
list_kd = kd_json['data']
for i in list_kd:
    kd_time = list_kd[i]['time']
    content = list_kd[i]['context']
    print(kd_time+' '+content)
    print('----------------------------------------')