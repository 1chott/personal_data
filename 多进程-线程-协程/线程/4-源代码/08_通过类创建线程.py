import  threading, time

# 1、定义类，继承threading.Thread
# 2、这个类threading.Thread中，有一个run()，派生类需要重写
# 3、只有这个run函数是线程函数，这个函数名字不能随便写
# 4、通过start()间接启动

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("正在服务餐桌1111111111111")
            time.sleep(1)


# 创建对象
obj = MyThread()
obj.start()

for i in range(5):
    print("主线程正在服务餐桌22222222222")
    time.sleep(1)

