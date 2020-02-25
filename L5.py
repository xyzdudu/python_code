import requests,re,bs4
url = 'https://y.qq.com/n/yqq/singer/0025NhlN2yWrP4.html'
res = requests.get(url)
bs = bs4.BeautifulSoup(res.text, 'html.parser')
items = bs.find('ul', class_='songlist__list').find_all('li')
for x in range(5):
    name = items[x].find('span', class_='songlist__songname_txt').text
    url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    refererurl = items[x].find(class_='songlist__songname_txt').find('a')['href']
    mid = items[x]['mid']
    
    # 这是请求歌词的url
    headers = {
        'origin':'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer':'https:'+refererurl,
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
    }
    params = {
    'nobase64': '1',
    'musicid': mid,
    '-': 'jsonp1',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
        }

    res_music = requests.get(url,headers=headers,params=params)
    # 发起请求
    json_music = res_music.json()
    lyric = json_music['lyric']
    for i in lyric.split('&#10'):
        music_str = re.sub("[A-Za-z0-9\\!\\%\\[\\]\\,\\。\\&\\#\\;]","",i)
        if music_str.strip():
            print(music_str);
    print('-----------------------------------')