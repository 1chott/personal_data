import urllib.request 
# 这个模块用户打开网页

# 打开一个网址，返回一个对象, 和打开文件一样
# 别忘了"http://"
req = urllib.request.urlopen("http://www.baidu.com")

# 读取内容
buf = req.read()

print("buf = ", buf)
