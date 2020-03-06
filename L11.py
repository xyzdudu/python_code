import requests, bs4, queue, time
# 本地Chrome浏览器设置方法
from selenium import  webdriver 
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from selenium.common.exceptions import NoSuchElementException

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://www.mtime.com/top/tv/top100/'

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options)

for x in range(10):
    global res
    if int(x) == 0:
        driver.get(url) 
    else:
        driver.get(url + 'index-' + str(int(x) + 1) + '.html')
    time.sleep(2)
    
    items = driver.find_element_by_class_name('top_list').find_element_by_id('asyncRatingRegion').find_elements_by_tag_name('li')
    for item in items:
        rank = item.find_element_by_class_name('number').text
        movcon = item.find_element_by_class_name('mov_con').find_elements_by_tag_name('p')
        name = item.find_element_by_class_name('mov_con').find_element_by_tag_name('h2').find_element_by_tag_name('a').text
        director = movcon[0].find_element_by_tag_name('a').text
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
            desc = '无'
        else:
            desc = mt3.text
            
        print(rank + ':' + name)
        print('导演：' +director)
        print('主演：',*list_actor)
        print('简介：' + desc)
        print('-------------------------------------------------')
    