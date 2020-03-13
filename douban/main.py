from scrapy import cmdline
import sys
import os
#导入cmdline模块,可以实现控制终端命令行。
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute(['scrapy','crawl','douban'])
#用execute（）方法，输入运行scrapy的命令