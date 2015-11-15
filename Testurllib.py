import urllib.request
req=urllib.request.urlopen(r'http://www.baidu.com')

print(req.readline())


