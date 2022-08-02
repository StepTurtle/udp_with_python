import socket
import pickle


class UdpSynchronousServer():
    def __init__(self, local_ip, local_port, buffer_size) -> None:
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size

        self.server_socket = None
        self.recieved_data = None
        self.from_where = None

        self.initializeSocket()

    def initializeSocket(self) -> None:
        self.server_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

        try:
            self.server_socket.bind((self.local_ip, self.local_port))
        except OSError:
            print(
                "Udp server already up to date on this address: [{}/{}]".format(self.local_ip, self.local_port))

        print("Udp synchronous server socket is up and ready to process.")

    def read(self) -> None:
        temp_data, self.from_where = self.server_socket.recvfrom(
            self.buffer_size)

        self.recieved_data = pickle.loads(temp_data)


class UdpSynchronousClient():
    def __init__(self, local_ip, local_port, buffer_size) -> None:
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = buffer_size

        self.client_socket = None

        self.initializeSocket()

    def initializeSocket(self) -> None:
        self.client_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

        print("Udp synchronous client socket is up and ready to process.")

    def write(self, data) -> None:
        self.client_socket.sendto(pickle.dumps(
            data), (self.local_ip, self.local_port))
