import urllib.request 
import gevent
from gevent import monkey

# 打补丁
monkey.patch_all()


url1 = "http://f.hiphotos.baidu.com/image/pic/item/3ac79f3df8dcd1007fde3f4e7e8b4710b9122f1b.jpg"

url2 = "http://c.hiphotos.baidu.com/image/pic/item/5243fbf2b21193138277eddd69380cd791238da2.jpg"

url3 = "http://h.hiphotos.baidu.com/image/pic/item/63d0f703918fa0ecf70575602a9759ee3c6ddb99.jpg"


def download_image(filename, url):
    # 打开一个网址，返回一个对象, 和打开文件一样
    # 别忘了"http://"
    req = urllib.request.urlopen(url)

    # 读取内容, 由于网页是一张图片，二进制
    buf = req.read()

    # 新建文件，往文件写内容，写入的就是图片内容
    with open(filename, "wb") as f:
        f.write(buf)

# 创建协程，等待所有协程结束
gevent.joinall([
    gevent.spawn(download_image, "1.jpg", url1),    
    gevent.spawn(download_image, "2.jpg", url2),    
    gevent.spawn(download_image, "3.jpg", url3)
    
])





