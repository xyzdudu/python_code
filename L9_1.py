from selenium import  webdriver 
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
import time

chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options = chrome_options) 
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php') # 访问页面
time.sleep(2)

userlogin = driver.find_element_by_id('user_login')
userlogin.send_keys('yyyyyy')
userpass = driver.find_element_by_id('user_pass')
userpass.send_keys('lyn596lyn59')
time.sleep(1)
button = driver.find_element_by_id('wp-submit')
time.sleep(1)
button.click()

time.sleep(3)

url = driver.find_element_by_partial_link_text('三').get_attribute('href')
driver.get(url) # 访问页面
time.sleep(2)

comment = driver.find_element_by_id('comment')
comment.send_keys('selenium,嘟嘟')
button = driver.find_element_by_id('submit')
time.sleep(1)
button.click()

driver.close()