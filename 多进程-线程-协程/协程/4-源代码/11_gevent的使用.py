import gevent

def work1():
   while True:
       print("work111111111111")


def work2():
    while True:
        print("work222222222222")

def main():
    # 创建gevent对象，指定协程处理函数
    p1 = gevent.spawn(work1)
    p2 = gevent.spawn(work2)

    # 主线程不会等待协程


if __name__ == '__main__':
    main()

