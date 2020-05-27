import time
import threading

def table1():
    print("正在服务餐桌1111111111111")
    time.sleep(1)

# threading.enumerate()功能：返回当前程序的线程信息，以列表方式返回
print("1111111 = ", threading.enumerate())

# 创建一个线程
t1 = threading.Thread(target=table1)
print("222222 = ", threading.enumerate())

# 启动线程
t1.start()
print("33333 = ", threading.enumerate())

