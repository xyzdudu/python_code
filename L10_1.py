import requests
from bs4 import BeautifulSoup

res_foods = requests.get('http://www.xiachufang.com/explore/')
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
list_foods = bs_foods.find_all('div',class_='info pure-u')

list_all = []

for food in list_foods:
    tag_a = food.find('a')
    name = tag_a.text[17:-13]
    URL = 'http://www.xiachufang.com'+tag_a['href']
    tag_p = food.find('p',class_='ing ellipsis')
    ingredients = tag_p.text[1:-1]
    list_all.append([name,URL,ingredients])
print(list_all)