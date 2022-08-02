from UdpSynchronous import UdpSynchronousClient

udp_client = UdpSynchronousClient("127.0.0.1", 20001, 1024)

counter = 0
while(True):
    udp_client.write(['a', 'b', counter])
    counter += 1
