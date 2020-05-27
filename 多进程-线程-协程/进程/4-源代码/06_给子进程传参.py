import multiprocessing, time

def fendian1(*args, **kwargs):
        print(args)
        print(kwargs)

def main():
    # 创建2进程
    # 功能：创建进程，返回一个对象
    # 参数使用和线程一样
    p1 = multiprocessing.Process(target=fendian1, args=("hello", 123), kwargs={"name":"mike", "addr":"sz"})

    # 不能直接调用进程处理函数，需要通过start间接调用
    p1.start()
    p1.join() #等待p1运行结束，才能往下执行
    print("父进程")



if __name__ == '__main__':
    main()

