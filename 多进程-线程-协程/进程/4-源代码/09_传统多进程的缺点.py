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
    # 创建进程，指定进程函数
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)
    p3 = multiprocessing.Process(target=work3)
    p4 = multiprocessing.Process(target=work4)

    p1.start()
    p2.start()
    p3.start()
    p4.start()


if __name__ == '__main__':
    main()