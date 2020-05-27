import socket
import threading

def send_msg(udp):
    ip = input("请输入需要发送的ip: ")
    port = int(input("请输入需要发送的port: "))
    while True:
        buf = input("请输入需要发送的内容：")
        udp.sendto(buf.encode(), (ip, port))

def recv_msg(udp):
    while True:
        recv_data = udp.recvfrom(1024)
        data, addr = recv_data
        print(addr, " >>>>>>>>>> ", data.decode())


def main():
    # 创建UDP套接字
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地网络地址
    udp.bind(("", 8899))

    # 创建2个线程
    t1 = threading.Thread(target=send_msg, args=(udp,))
    t2 = threading.Thread(target=recv_msg, args=(udp,))

    # 启动线程
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
