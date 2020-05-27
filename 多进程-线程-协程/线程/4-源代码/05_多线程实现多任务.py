import time
import threading

def table1():
    for i in range(5):
        print("正在服务餐桌1111111111111")
        time.sleep(1)

def table2():
    for i in range(5):
        print("正在服务餐桌222222222222")
        time.sleep(1)

def main():
    """程序入口"""

    # 创建2个线程
    # 功能：创建线程，同时指定线程处理函数，这里只是创建线程，线程还没有起作用
    # 参数：指定的线程处理函数，参数需要以命名方式传递参数，这里传递的是函数的名字，没有()
    # 返回值：就是一个线程对象
    t1 = threading.Thread(target=table1)
    t2 = threading.Thread(target=table2)

    # 启动线程
    # 线程函数，不是直接调用，通过start()间接启动
    t1.start()
    t2.start()


    for i in range(5):
        print("主线程正在服务餐桌3333333333")
        time.sleep(1)


if __name__ == '__main__':
    main()