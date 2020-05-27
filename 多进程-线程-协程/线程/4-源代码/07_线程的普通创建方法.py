import  threading, time

def table1():
    for i in range(5):
        print("正在服务餐桌1111111111111")
        time.sleep(1)

# 1、定义一个普通函数，专门用于线程处理函数，这个函数名字没有要求
# 2、创建线程函数，指定线程函数
# 3、启动

t1 = threading.Thread(target=table1)

t1.start()

for i in range(5):
    print("主线程正在服务餐桌22222222222")
    time.sleep(1)

