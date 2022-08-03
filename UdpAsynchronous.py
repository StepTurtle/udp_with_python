import socket
import asyncoro
import pickle


class UdpAsynchronousServer():
    def __init__(self, local_ip, local_port, buffer_size) -> None:
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size

        self.server_socket = None
        self.recieved_data = None
        self.from_where = None

        self.initializeSocket()

    def initializeSocket(self) -> None:
        self.server_socket = asyncoro.AsynCoroSocket(
            socket.socket(socket.AF_INET, socket.SOCK_DGRAM))

        try:
            self.server_socket.bind((self.local_ip, self.local_port))
        except:
            print(
                "Udp server already up to date on this address: [{}/{}]".format(self.local_ip, self.local_port))

        print("Udp asynchronous server socket is up and ready to process.")

    def read(self) -> None:
        asyncoro.Coro(self.get_data)

    def get_data(self) -> None:
        temp_data, self.from_where = yield self.server_socket.recvfrom(self.buffer_size)

        self.recieved_data = pickle.loads(temp_data)
