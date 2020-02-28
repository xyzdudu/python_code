# 引入requests
import requests, bs4
# 封装headers
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 写入网址
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 封装参数
params={
    'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset':'10',
    'limit':'10',
    'sort_by':'create',
    }
# 发送请求，并把响应内容赋值到变量res里面
res=requests.get(url,headers=headers,params=params)
# 确认请求成功
print(res.status_code)
# 用json()方法解析response对象，并赋值给变量articles
# articles=res.json()
bs = bs4.BeautifulSoup(res.text, 'html.parser')
items = bs.find(class_='ListShortcut').find(class_='List').find_all(class_='List-item')
for item in items:
    name = item.find('h2').text
    print(name)