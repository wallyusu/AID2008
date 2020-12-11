"""
向京东官网发请求，拿到响应内容
"""
import requests

resp = requests.get(url='https://www.jd.com/')
# print(resp)

# text属性：获取响应内容 - 字符串
html = resp.text  # 获取源代码
# print(html)

# content 属性：获取响应内容 - 字节串  用来抓取图片、音频、文件...
html = resp.content
# print(html)

# status_code属性：获取HTTP响应码
code = resp.status_code
# url属性： 获取返回实际数据的url地址 用到不多
url = resp.url
# print(code,url)