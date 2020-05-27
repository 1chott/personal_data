import socket, time, gevent
from gevent import monkey

# 打补丁
monkey.patch_all()

def send_msg(udp):
    while True:
        udp.sendto("hello".encode(), ("192.168.25.91", 7777))
        time.sleep(0.5)

def recv_msg(udp):
    while True:
        data = udp.recvfrom(1024)
        print("data = ", data)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind(("", 8888))

# 开协程， 分别接受和发送
gevent.joinall([
    gevent.spawn(send_msg, udp),    
    gevent.spawn(recv_msg, udp)   
])


