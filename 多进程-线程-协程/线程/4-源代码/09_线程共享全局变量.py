import time
import threading

# 定义一个全局变量
g_num = 555

# 线程1处理函数修改内容
def table1():
    global  g_num
    g_num = 666
    print("tabel 111111 = ", g_num)

# 线程2处理函数取内容
def table2():
    global  g_num
    print("tabel 22222 = ", g_num)


def main():
    """程序入口"""
    # 创建2个线程
    t1 = threading.Thread(target=table1)
    t2 = threading.Thread(target=table2)

    # 启动线程
    t1.start()

    time.sleep(1) #目的为了让t1先执行完
    t2.start()
    time.sleep(1)  # 目的为了让t2先执行完
    print("main 3333 = ", g_num)




if __name__ == '__main__':
    main()