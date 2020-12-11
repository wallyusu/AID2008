"""
百度贴吧爬取案例
"""
import requests
from urllib import parse

# 拼接URL地址:：https://www.baidu.com/s?wd=d
word = input('请输入关键字： ')
params = parse.urlencode({'wd': word})
url = 'https://www.baidu.com/s?' + params
headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
# 2. 发请求获取响应
html = requests.get(url=url,
                       headers=headers).text
# 具体headers可以百度搜索: 常见 User-Agent 大全,选择一个请求地址
# 3. 数据处理
filename = '{}.html'.format(word)
with open(filename,'w') as f:
    f.write(html)
    print('{}已抓取完成！'.format(word))