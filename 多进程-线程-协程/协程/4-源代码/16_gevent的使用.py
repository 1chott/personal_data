import gevent

#协程利用等待的时间来切换

def work1(n):
    for i in range(n):
        print("work111111111111")
        gevent.sleep(0.5)


def work2(n):
    for i in range(n):
        print("work222222222222")
        gevent.sleep(0.5)

def main():
    # 创建gevent对象，指定协程处理函数
    p1 = gevent.spawn(work1, 5)
    p2 = gevent.spawn(work2, 8)

    # 主线程不会等待协程
    # 协程本质上是单任务
    # p1协程函数运行完毕，说明这个等待完成，说明join可以往下走
    # 主线程结束，整个程序也结束，其它协程函数没有运行完，也会结束
    p1.join() # 等待p1协程运行完毕
    p2.join()

if __name__ == '__main__':
    main()

