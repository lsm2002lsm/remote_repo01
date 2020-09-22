import time

if __name__ == '__main__':
    ltime = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
    print(ltime)
    print(type(ltime))

    ndate = time.strftime("%Y%m%d", time.localtime())
    print(ndate)
    print(type(ndate))

    ntime = time.strftime("%H%M%S", time.localtime())
    print(ntime)
    print(type(ntime))