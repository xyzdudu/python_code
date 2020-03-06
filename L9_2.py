from selenium import  webdriver 
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('酱酱')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()

time.sleep(2)

contents = driver.find_elements_by_class_name('content')
etitle = contents[0].find_element_by_tag_name('h1').text
ctitle = contents[1].find_element_by_tag_name('h1').text
econtent = contents[0].find_element_by_tag_name('p').text
ccontent = contents[1].find_element_by_tag_name('p').text

print(etitle)
print(econtent)
print('----------------------')
print(ctitle)
print(ccontent)

