import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')

def food():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
    list_foods = bs_foods.find_all('div', class_='info pure-u')

    strfood = ''

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com' + tag_a['href']
        tag_p = food.find('p', class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        strfood += '菜名：' + name + '\n'
        strfood += '链接：' + URL + '\n'
        strfood += '材料：' + ingredients + '\n'
        strfood += '------------------------------------------------------\n'
    return strfood

def send_email(food):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= food
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '本周最佳菜谱'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    foodlist = food()
    send_email(foodlist)
    print('任务完成')

schedule.every().friday.do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)
