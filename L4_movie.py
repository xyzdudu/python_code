import requests, random, bs4, urllib
# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

moviename = input('输入电影名：')
moviename_gbk = moviename.encode('gbk')

url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+urllib.parse.quote(moviename_gbk)
print(url)
res = requests.get(url, headers=headers)
bs = bs4.BeautifulSoup(res.text, 'html.parser')
items = bs.find(class_='co_content8').find('ul').find_all('table')
if len(items) > 0:
    link = items[0].find('a')['href']
    targeturl = 'http://s.ygdy8.com' + link
    res = requests.get(targeturl, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    downloadurl = bs.find(class_='co_content8').find('a').text
    print(downloadurl)
    