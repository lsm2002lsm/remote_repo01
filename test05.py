# import uuid
#
# print(uuid.uuid4())
#
# print(uuid.uuid5(uuid.NAMESPACE_DNS, 'qilu-pharma.com'))

import time
import datetime

t = time.time()

print(t)  # 原始时间数据
print(int(t))  # 秒级时间戳
print(int(round(t * 1000)))  # 毫秒级时间戳
print(int(round(t * 1000000)))  # 微秒级时间戳
