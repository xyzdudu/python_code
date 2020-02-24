import re

content = '
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: csrftoken=WxlTM1AGpITnXam8KqlkvFEN6jLuNNKZOctEQ8mxjzM; WWWID=WWW633095FA395B4A10A82585192F6F001A; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1582521935; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1582521935
Host: www.kuaidi100.com
Referer: https://www.kuaidi100.com/
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
X-Requested-With: XMLHttpRequest'

# 每次只要把content的内容换掉就行

text0 = re.findall('(.*?)\:(.*?)\n',content)
#print(text0)
text_final =''
for i in text0:
    text1 = '\''+i[0]+'\':\''+i[1]+'\',\n'
    text_final = text_final +text1
print(text_final.replace(' ',''))