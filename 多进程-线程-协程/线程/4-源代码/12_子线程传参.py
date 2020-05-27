import threading

# 线程1处理函数修改内容
def table1(tmp):
    print(tmp)

def main():
    """程序入口"""
    # 创建2个线程
    t1 = threading.Thread(target=table1,  args=((11,"mike"), ))

    # 启动线程
    t1.start()

if __name__ == '__main__':
    main()