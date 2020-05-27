import time
import threading


def work1():
   while True:
       print("work111111111111")


def work2():
    while True:
        print("work222222222222")


def main():
    # 指定线程处理函数
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
