#这是爬取豆瓣电影Top250，并存为本地csv的代码

import requests,  random, csv
import smtplib
from bs4 import BeautifulSoup
from urllib.request import quote
from email.mime.text import MIMEText
from email.header import Header

def top250():
    csv_file=open('movieTop.csv', 'w', newline='',encoding='utf-8')
    writer = csv.writer(csv_file)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    movielist = []
    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url, headers=headers)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            title = titles.find('span', class_="title").text
            list1 = [title]
            movielist.append(title)
            writer.writerow(list1)
    csv_file.close()
    return [movielist[random.randint(0,249)], movielist[random.randint(0,249)], movielist[random.randint(0,249)]]

def download(moviesname):
    content = ''
    for name in moviesname:
        gbkmovie = name.encode('gbk')
        urlsearch = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+quote(gbkmovie)
        content += name + '\n' + urlsearch + '\n'
    return content

def sendmail(account):
    mailhost='smtp.qq.com'
    #把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP()
    #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
    qqmail.connect(mailhost,25)
    #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
    #以上，皆为连接服务器。

    account = input('请输入你的邮箱：')
    #获取邮箱账号，为字符串格式
    password = input('请输入你的密码：')
    #获取邮箱密码，为字符串格式
    qqmail.login(account,password)
    #登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
    #以上，皆为登录邮箱。
    receiver=input('请输入收件人的邮箱：')
    #获取收件人的邮箱。

    #content为上面的电影链接
    #输入你的邮件正文，为字符串格式
    message = MIMEText(content, 'plain', 'utf-8')
    #实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
    subject = '电影链接'
    #输入你的邮件主题，为字符串格式
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

movielist = top250()
content = download(movielist)
sendmail(content)
