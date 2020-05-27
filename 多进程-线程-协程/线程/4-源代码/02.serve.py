import socket

# 创建TCP套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 套接字端口复用
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定
tcp_socket.bind(("", 8888))

# 监听
tcp_socket.listen(128)

# 取出客户，返回一个新的套接字和客户地址
new_socket, cli_addr = tcp_socket.accept()
print(cli_addr, "链接成功")

# 接收文件名
recv_data = new_socket.recv(1024)
print(recv_data.decode())
filename = recv_data.decode()

# 以用户发过来的文件名作为目标
try: # 打开成功, 只读二进制方式打开
    with open(filename, "rb") as f:
        content = f.read() # 读取文件内容

    # 发送文件内容
    new_socket.send(content)
except Exception as ret: #打开失败
    print("打开文件失败, err = ", ret)


new_socket.close()
tcp_socket.close()
