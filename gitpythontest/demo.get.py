# -*- coding: utf-8 -*-
from requests.api import get

params={
    'phone':'18602355173',
    'key':'b07c85237609fc6005e5ef8f81a7f2fc',
    'dtype':'json'
}

response = get("http://apis.juhe.cn/mobile/get",params=params)
print(response.text)
print(type(response.text))
print(type(eval(response.text)))

print(response.status_code)
print(response.headers)

rs = eval(response.text)
if rs['error_code']==0:
    print('测试通过')