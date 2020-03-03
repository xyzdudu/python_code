# 本地Chrome浏览器设置方法
from selenium import  webdriver 
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类

import time
'''
driver = webdriver.Chrome() 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') 
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(1)
driver.close()
'''
'''
driver = webdriver.Chrome() 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') 
time.sleep(2)

labels = driver.find_elements_by_tag_name('label') # 根据标签名提取所有元素
for label in labels:
    print(label.text)
driver.close() # 关闭浏览器
'''

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) 
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

button = driver.find_element_by_link_text('点击加载更多')
time.sleep(1)
button.click()

time.sleep(2)

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
print(len(comments)) # 打印获取到的评论个数
for comment in comments: # 循环
    sweet = comment.find_element_by_tag_name('p') # 找到评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论
driver.close() # 关闭浏览器