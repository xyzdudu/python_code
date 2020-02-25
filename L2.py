import requests
from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res = requests.get (url)
soup = BeautifulSoup(res.text,'html.parser')
#items = soup.find_all(class_='comments-area')
'''
for item in items:
    ol = item.find('ol')
    print(ol.text)
'''
'''
items = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')
for item in items:
    print(item.text.strip())
'''

items = soup.find('section').find('ol').find_all('li')
for item in items:
    bookname = item.find('h3')
    stars = item.find('p').find_all('i')
    price = item.find(class_='product_price').find('p',class_='price_color')
    print('书名：' + bookname.text + ' 评分：'+str(len(stars)) + ' 价格：' + price.text)
