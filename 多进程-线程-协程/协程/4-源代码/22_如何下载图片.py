import urllib.request 
# 这个模块用户打开网页

url1 = "http://f.hiphotos.baidu.com/image/pic/item/3ac79f3df8dcd1007fde3f4e7e8b4710b9122f1b.jpg"

# 打开一个网址，返回一个对象, 和打开文件一样
# 别忘了"http://"
req = urllib.request.urlopen(url1)

# 读取内容, 由于网页是一张图片，二进制
buf = req.read()

# 新建文件，往文件写内容，写入的就是图片内容
with open("1.jpg", "wb") as f:
    f.write(buf)
