import time, multiprocessing, random, os

def work1():
    print("1 开始执行： pid = ", os.getpid())
    s_time = time.time() #开始时间
    # random.random()产生随机数在0~1之间
    #print(random.random() )
    time.sleep(random.random())

    e_time = time.time()  # 结束时间
    print("1 结束， 耗时 %.2f, pid = %d"%(e_time - s_time, os.getpid()))

def work2():
    print("2 开始执行： pid = ", os.getpid())
    s_time = time.time() #开始时间
    # random.random()产生随机数在0~1之间
    #print(random.random() )
    time.sleep(random.random())

    e_time = time.time()  # 结束时间
    print("2 结束， 耗时 %.2f, pid = %d"%(e_time - s_time, os.getpid()))

def work3():
    print("3 开始执行： pid = ", os.getpid())
    s_time = time.time() #开始时间
    # random.random()产生随机数在0~1之间
    #print(random.random() )
    time.sleep(random.random())

    e_time = time.time()  # 结束时间
    print("3 结束， 耗时 %.2f, pid = %d"%(e_time - s_time, os.getpid()))

def work4():
    print("4 开始执行： pid = ", os.getpid())
    s_time = time.time() #开始时间
    # random.random()产生随机数在0~1之间
    #print(random.random() )
    time.sleep(random.random())

    e_time = time.time()  # 结束时间
    print("4 结束， 耗时 %.2f, pid = %d"%(e_time - s_time, os.getpid()))

def main():
    # 创建进程池，指定有1给子进程
    po = multiprocessing.Pool(1)

    # 把函数加入到队列中，进程池自动管理
    # 加入一个任务，才可以工作
    po.apply_async(work1)
    time.sleep(2)
    po.apply_async(work2)
    time.sleep(2)
    po.apply_async(work3)
    time.sleep(2)
    po.apply_async(work4)
    time.sleep(2)




if __name__ == '__main__':
    main()