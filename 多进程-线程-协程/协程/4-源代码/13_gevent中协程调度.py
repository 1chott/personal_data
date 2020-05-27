import gevent
# gevent协程调用的策略，利用这个单任务等待的时间，用于切换任务

def work1():
   while True:
       print("work111111111111")
       gevent.sleep(0.1)


def work2():
    while True:
        print("work222222222222")
        gevent.sleep(0.5)

def main():
    # 创建gevent对象，指定协程处理函数
    p1 = gevent.spawn(work1)
    p2 = gevent.spawn(work2)

    # 主线程不会等待协程
    # 不让主线程结束
    while True:
        print("33333333333")
        gevent.sleep(0.5)


if __name__ == '__main__':
    main()

