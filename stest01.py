import urllib.request

# url = "http://www.baidu.com/"
url = "http://www.qilu-pharma.com/"

response = urllib.request.urlopen(url=url)
# print(response.read().decode())
# with open('qilu.html', 'w', encoding='utf-8') as fp:
#     fp.write(response.read().decode())

# print(response.geturl())  #获取请求的URL

# print(response.getheaders())  #获取头部信息

# print(response.getcode())  #获取状态码


