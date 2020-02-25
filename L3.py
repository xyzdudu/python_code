import requests
from bs4 import BeautifulSoup
url = 'http://www.xiachufang.com/explore/'
res = requests.get (url)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.find(class_='normal-recipe-list').find('ul',class_='list').find_all('li')
itemlist = []
for item in items:
    name = item.find(class_='info pure-u').find('p',class_='name')
    url = name.find('a', href=True)
    materials = item.find(class_='info pure-u').find_all(class_='ing ellipsis')
    materiallist = []
    for material in materials:
        materiallist.append(material.text.strip())
    itemlist.append([name.text.strip(), url['href'],materiallist])
print(itemlist)