import requests, json

url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {
    'origin':
    'http://ictclas.nlpir.org',
    'referer':
    'http://ictclas.nlpir.org/nlpir/',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

words = input('输入单词：')
data = {'content': words}

res = requests.post(url, data=data, headers=headers)
w2vlist = json.loads(res.text)
for item in w2vlist['w2vlist']:
    strlist = item.split(',')
    print('联想词汇：' + strlist[0] + ',系数：' + strlist[1])
