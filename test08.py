import time

dict_data = [
    {
        'SPIDER_DATE': '20200908',
        'ZSUBMITTIME': '1599099784000',
        'ZTOTALDISTRIBUTECOUNT': '',
        'ZTOTALWAREHOUSECOUNT': ''
    },

    {
        'SPIDER_DATE': '20200908',
        'ZSUBMITTIME': '1599099784000',
        'ZTOTALDISTRIBUTECOUNT': '',
        'ZTOTALWAREHOUSECOUNT': ''
    },

]

for data in dict_data:
    print(data)
    for k in data.keys():
        if k == 'ZSUBMITTIME':
            # print(data[i])
            timeNum = int(data[k])
            timeStamp = float(timeNum / 1000)
            timeArray = time.localtime(timeStamp)
            data[k] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            # print(data[i])
        if k == 'ZTOTALDISTRIBUTECOUNT' and data[k] == '':
            data[k] = 0

        if k == 'ZTOTALWAREHOUSECOUNT' and data[k] == '':
            data[k] = 0
    print(data)

print(dict_data)


print("123")
