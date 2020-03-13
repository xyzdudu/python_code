import scrapy, bs4
from ..items import DangdangItem

class DoubanSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = []
    for x in range(3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(x + 1)
        start_urls.append(url)

    def parse(self, response):
        #parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        #用BeautifulSoup解析response。
        datas = bs.find('ul', class_='bang_list_mode').find_all('li')
        #用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        for data in datas:
            #遍历data。
            item = DangdangItem()
            #实例化DoubanItem这个类。
            item['name'] = data.find(class_='name').find('a').text
            #提取出书名，并把这个数据放回DoubanItem类的title属性里。
            item['author'] = data.find(class_='publisher_info').find('a').text
            #提取出出版信息，并把这个数据放回DoubanItem类的publish里。
            item['price'] = data.find(class_='price').find('span', class_='price_n').text
            #提取出评分，并把这个数据放回DoubanItem类的score属性里。
            print(item['name'])
            #打印书名。
            yield item
            #yield item是把获得的item传递给引擎。