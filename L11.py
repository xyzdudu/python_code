import requests, bs4, time, gevent, csv, re
# 本地Chrome浏览器设置方法
from selenium import  webdriver 
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from selenium.common.exceptions import NoSuchElementException
from gevent import monkey
from gevent.queue import Queue
from bs4 import BeautifulSoup

start = time.time()

# monkey.patch_all()

work = Queue()

headers = {
    'referer':'http://www.mtime.com/top/tv/top100/',
    'Cookie':'td_cookie=2128675784; waf_cookie=e48d0839-7408-4ada3cd7a419623493265433af737700d13a; _userCode_=202036118275321; _userIdentity_=202036118272158; DefaultCity-CookieKey=364; DefaultDistrict-CookieKey=0; _tt_=3D296E3A4A952141AC771C33C4E19049; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1583464109; __utmc=196937584; __utmz=196937584.1583464111.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=196937584.1110767174.1583464111.1583740981.1583743231.7; __utmb=196937584.4.10.1583743231; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1583743512; _ydclearance=88616c47a0c5b1753b169957-6496-4bdd-8639-10338ad38a1f-1583751880',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式

csv_file=open('movieTop250.csv', 'w', newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['排名', '电影名', '导演', '主演', '简介'])
url_list = []

url = 'http://www.mtime.com/top/tv/top100/'
for x in range(10):
    if int(x) == 0:
        url_list.append(url) 
    else:
        url_list.append(url + 'index-' + str(int(x) + 1) + '.html')


for url in url_list:
#遍历url_list
    work.put_nowait(url)
    #用put_nowait()函数可以把网址都放进队列里。

def crawler():
    while not work.empty():
        targeturl = work.get_nowait()
        #用get_nowait()函数可以把队列里的网址都取出。
        driverurl(targeturl) 

def driverurl(url):
    '''
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(url)
    time.sleep(2)
    
    items = driver.find_element_by_class_name('top_list').find_element_by_id('asyncRatingRegion').find_elements_by_tag_name('li')
    for item in items:
        rank = item.find_element_by_class_name('number').text
        movcon = item.find_element_by_class_name('mov_con').find_elements_by_tag_name('p')
        name = item.find_element_by_class_name('mov_con').find_element_by_tag_name('h2').find_element_by_tag_name('a').text
        if len(movcon) > 0:
            try:
                director = movcon[0].find_element_by_tag_name('a').text
            except NoSuchElementException as e:
                director = ''
        else:
            director = ''
        if len(movcon) > 1:
            actors = movcon[1].find_elements_by_tag_name('a')
        else:
            actors = []
        list_actor = []
        for actor in actors:
            list_actor.append(actor.text)
        try:
            mt3 = item.find_element_by_class_name('mov_con').find_element_by_class_name('mt3')
        except NoSuchElementException as e:
            desc = ''
        else:
            desc = mt3.text
            
        print(rank + ':' + name)
        print('导演：' +director)
        print('主演：',*list_actor)
        print('简介：' + desc)
        print('-------------------------------------------------')
        writer.writerow([rank, name, director, *list_actor, desc])
    '''

    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    items = bs.find(class_='top_list').find('ul').find_all('li')
    for item in items:
        rank = item.find('em').text
        movcon = item.find(class_='mov_con')
        name = movcon.find('h2').find('a').text
        plist = movcon.find_all('p')
        director = ''
        list_actor = []
        actors = []
        for p in plist:
            if re.match('导演', p.text) != None:
                director = p.find('a').text
            elif re.match('主演', p.text) != None:
                actors = p.find_all('a')
        for actor in actors:
            list_actor.append(actor.text)

        desc = ''
        try:
            desc = movcon.find('p', class_='mt3').text
        except:
            pass
        print(rank + ':' + name)
        print('导演：' +director)
        print('主演：',*list_actor)
        print('简介：' + desc)
        print('-------------------------------------------------')
        writer.writerow([rank, name, director, *list_actor, desc])

tasks_list  = [ ]
#创建空的任务列表
for x in range(2):
#相当于创建了2个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn()函数创建执行crawler()函数的任务。
    tasks_list.append(task)
    #往任务列表添加任务。
gevent.joinall(tasks_list)
csv_file.close()
end = time.time()
print(end-start)