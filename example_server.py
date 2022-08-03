from UdpAsynchronous import UdpAsynchronousServer

udp_server = UdpAsynchronousServer("127.0.0.1", 20001, 1024)

while(True):
    udp_server.read()
    print(udp_server.recieved_data)
    print(udp_server.from_where)
