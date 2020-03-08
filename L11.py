import requests, bs4, time, gevent, csv
# 本地Chrome浏览器设置方法
from selenium import  webdriver 
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from selenium.common.exceptions import NoSuchElementException
from gevent import monkey
from gevent.queue import Queue

start = time.time()

# monkey.patch_all()

work = Queue()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

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