import gevent, time
from gevent import monkey

#协程利用等待的时间来切换
# 打补丁，只要有阻塞耗时(大部分)的地方，就算不是gevent.sleep(), 也会自动切换
 monkey.patch_all()

def work1(n):
    for i in range(n):
        print("work111111111111")
        time.sleep(0.5)


def work2(n):
    for i in range(n):
        print("work222222222222")
        time.sleep(0.5)

def main():
    # 创建gevent对象，指定协程处理函数
    # 等待所有的协程函数执行完毕
    gevent.joinall([
        gevent.spawn(work1, 5),
        gevent.spawn(work2, 8)
    ])

if __name__ == '__main__':
    main()

