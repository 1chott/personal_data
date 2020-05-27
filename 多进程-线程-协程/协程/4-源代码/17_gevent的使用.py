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
    # 等待所有的协程函数执行完毕
    gevent.joinall([
        gevent.spawn(work1, 5),
        gevent.spawn(work2, 8)
    ])

if __name__ == '__main__':
    main()

