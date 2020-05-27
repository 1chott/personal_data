import time

def table1():
    for i in range(5):
        print("正在服务餐桌1111111111111")
        time.sleep(1)

def table2():
    for i in range(5):
        print("正在服务餐桌222222222222")
        time.sleep(1)

def main():
    """程序入口"""

    table1()
    table2()

if __name__ == '__main__':
    main()