import socket

# 处理客户的数据，参数为成功连接的客户端套接字
def handle_client(new_socket):
    # 接收客户端的数据，客户没有发送内容，阻塞，注意，使用服务套接字接收内容
    recv_data = new_socket.recv(1024)
    print("*"*40)
    print("recv_data = ", recv_data.decode())


    send_data = "HTTP/1.1 200 OK\r\n" # 状态行
    send_data += "\r\n"               # 空行
    send_data += "ok"

    # 给对方回复数据，使用新的套接字
    new_socket.send(send_data.encode())

    # 关闭套接字
    new_socket.close()


def main():
    # 创建TCP套接字(监听、链接套接字)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定
    tcp_socket.bind(("", 8888))

    # 监听，将套接字变为被动，系统创建一个链接队列
    tcp_socket.listen(128)
    while True:
        # 取出成功链接的客户，返回一个新的套接字（服务套接字），用户地址，如果没有客户连接，也会阻塞
        new_socket, cli_addr = tcp_socket.accept()
        print(cli_addr, "成功连接")
        
        # 通过函数处理
        handle_client(new_socket)


    tcp_socket.close()

if __name__ == "__main__":
    main()
