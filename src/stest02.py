import urllib.request
import ssl

# https 跳过证书验证
ssl._create_default_https_context = ssl._create_unverified_context

image_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596445179096&di=0ca4d9f66a0742e451b2c2c0848d5265&imgtype=0&src=http%3A%2F%2F01.minipic.eastday.com%2F20170330%2F20170330044723_a0c69f758cc90e87e8c8e620eb55308e_2.jpeg'

# response = urllib.request.urlopen(image_url)
#
# with open('biz.jpg', 'wb') as fp:
#     fp.write(response.read())

urllib.request.urlretrieve(image_url, 'biz1.jpg')
