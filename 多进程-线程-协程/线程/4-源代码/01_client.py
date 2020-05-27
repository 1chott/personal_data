import socket

# 创建TCP套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 主动链接
tcp_socket.connect(("192.168.25.112", 8888))

filename = input("请输入需要下载的文件名：")
tcp_socket.send(filename.encode())

# 接收服务器发送的文件内容
recv_data = tcp_socket.recv(1024)
print("文件内容为：", recv_data.decode())

if recv_data:
    with open("[new]"+filename, "wb") as f:
        # 由于网络上的数据是二进制，我们也是以二进制新建文件
        # 所以不需要转码
        f.write(recv_data)
        print("下载成功")

else:
    print("下载失败")

# 关闭套接字
tcp_socket.close()
