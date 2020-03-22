#导入模块：
import scrapy
import bs4
from ..items import DoubanbookItem

class DouBanBookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
    #parse是默认处理response的方法
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('tr', class_="item")
        for data in datas:
            a = data.find_all('a')[1]
            bookurl = a['href']
            yield scrapy.Request(bookurl, callback=self.parse_book)

    def parse_book(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        bookname = bs.find('h1').find('span').text
        print(bookname)
        datas = bs.find(class_='comment-list hot show').find_all('li')
        print(len(datas))
        for data in datas:
            item = DoubanbookItem()
            item['bookname'] = bookname
            item['id'] = data.find(class_='comment').find('h3').find('span', class_='comment-info').find('a').text
            item['content'] = data.find('span', class_='short').text
            yield item
