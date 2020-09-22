import urllib.request
import urllib.parse
from lxml import etree
import time
import os


def handle_request(url, page):
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))
    # print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse_content(content):
    tree = etree.HTML(content)
    # 懒加载
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # print(image_list)
    # print(len(image_list))
    for img in image_list:
        download_image(img)


def download_image(img):
    dirpath = 'meinv'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    filename = os.path.basename(img)
    filepath = os.path.join(dirpath, filename)

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    request = urllib.request.Request(url=img, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'
    start_page = int(input('开始页:'))
    end_page = int(input('结束页:'))
    for page in range(start_page, end_page + 1):
        print('开始爬取第%s页' % page)
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        print('结束爬取第%s页' % page)
        time.sleep(2)


if __name__ == '__main__':
    main()
