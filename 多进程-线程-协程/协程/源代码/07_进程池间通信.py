import multiprocessing, time

def write(q):
    buf = "hello"
    for v in buf:
        # 参数就是放的内容
        q.put(v) #put后最好加一个简单的延时
        print("放的内容为：", v)
        time.sleep(0.1)

def read(q):
    # q.empty() # 这个队列是否为空，为空返回True
    while True:
        # 从队列中取内容，返回值为取出的内容
        v = q.get()
        print("取出 v = ", v)

        if q.empty(): #如果为空，跳出循环
            break

def main():

    # 创建进程池间通信的队列，和普通队列创建不一样，返回值为对象
    q = multiprocessing.Manager().Queue()

    #创建进程池，只有一个1进程，服务2个函数
    po = multiprocessing.Pool(1)

    # 函数添加到进程队列中
    po.apply_async(write, args=(q,))
    po.apply_async(read, args=(q,))

    # 等待进程池工作完毕
    po.close()
    po.join()




if __name__ == '__main__':
    main()