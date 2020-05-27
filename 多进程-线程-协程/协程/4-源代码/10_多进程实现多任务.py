import multiprocessing, time

def work1():
   while True:
       print("work111111111111")


def work2():
    while True:
        print("work222222222222")

def main():
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()

