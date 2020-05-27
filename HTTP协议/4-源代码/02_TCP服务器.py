import socket

# 创建TCP套接字(监听、链接套接字)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定
tcp_socket.bind(("", 9988))

# 监听，将套接字变为被动，系统创建一个链接队列
tcp_socket.listen(128)

# 取出成功链接的客户，返回一个新的套接字（服务套接字），用户地址，如果没有客户连接，也会阻塞
new_socket, cli_addr = tcp_socket.accept()
print(cli_addr, "成功连接")

# 接收客户端的数据，客户没有发送内容，阻塞，注意，使用服务套接字接收内容
recv_data = new_socket.recv(1024)
print(cli_addr, " >>>>>>>> ", recv_data.decode())

# 给对方回复数据，使用新的套接字
new_socket.send("ok".encode())

# 关闭套接字
new_socket.close()
tcp_socket.close()
