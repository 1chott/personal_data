import time, multiprocessing, random, os

def work(n):
    print("%d 开始执行： pid = %d"%(n, os.getpid()))
    s_time = time.time() #开始时间
    # random.random()产生随机数在0~1之间
    #print(random.random() )
    time.sleep(random.random())

    e_time = time.time()  # 结束时间
    print("%d 结束， 耗时 %.2f, pid = %d"%(n, e_time - s_time, os.getpid()))


def main():
    # 创建一个进程池，有3个子进程
    # 返回一个对象
    po = multiprocessing.Pool(3)

    # 创建进程，指定进程函数
    # 耗时在创建进程，销毁进程
    for i in range(10):
        # 将函数添加到进程队列，没有添加到进程中
        po.apply_async(work, args=(i,))

    po.close() #不能再往队列中添加任务
    po.join() # 等待进程池工作完毕


if __name__ == '__main__':
    main()