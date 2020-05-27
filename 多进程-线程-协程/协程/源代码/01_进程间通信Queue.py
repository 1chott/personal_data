import multiprocessing, time

# 这个进程往队列写东西
def fendian1(q):
    buf = "hello"
    for v in buf:
        # 参数就是放的内容
        q.put(v) #put后最好加一个简单的延时
        print("放的内容为：", v)
        time.sleep(1)

# 这个进程就取内容
def fendian2(q):
    # q.empty() # 这个队列是否为空，为空返回True
    while True:
        # 从队列中取内容，返回值为取出的内容
        v = q.get()
        print("取出 v = ", v)

        if q.empty(): #如果为空，跳出循环
            break

def main():
    # 创建一个队列，队列可以理解为管道，一端写内容，另外一端取内容
    # 返回值，就是队列对象，可以传参，写了一个数字，不写代表个数不做限制
    q = multiprocessing.Queue()

    # 创建2进程
    # 功能：创建进程，返回一个对象
    # 参数使用和线程一样
    p1 = multiprocessing.Process(target=fendian1, args=(q,))
    p2 = multiprocessing.Process(target=fendian2, args=(q,))

    # 不能直接调用进程处理函数，需要通过start间接调用
    p1.start()
    # 保证p1先执行完毕
    p1.join()

    p2.start()


if __name__ == '__main__':
    main()

