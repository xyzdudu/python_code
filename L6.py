import openpyxl, requests, random, bs4, csv
wb=openpyxl.Workbook() 
sheet=wb.active
sheet.title='new title'
sheet['A1'] = '电影名'
sheet['B1'] = '评分'
sheet['C1'] = '推荐语'
sheet['D1'] = '链接'
rows= []

csv_file = open('movietop250.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = ''
        if titles.find('span',class_="inq") is None:
            tes  = '暂无推荐语'
        else:
            tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']
        sheet.append([title, comment, tes, url_movie])
        writer.writerow([title, comment, tes, url_movie])
        #print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)

#for i in rows:
    #sheet.append(i)
wb.save('movietop250.xlsx')
csv_file.close()
print('保存完成')