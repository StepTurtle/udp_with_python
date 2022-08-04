## <div align="center">udp_with_python</div>

Small scripts for communicate with udp in python.

## <div align="center">Quick Start Examples</div>

In your codes you can simply use udp classes like this;

<details open>
<summary>Server</summary>

```python
from UdpAsynchronous import UdpAsynchronousServer

udp_server = UdpAsynchronousServer("127.0.0.1", 20001, 1024) # create object from server class.

while(True):
    udp_server.read() # you can receive datas with loop.
    print(udp_server.recieved_data)
    print(udp_server.from_where)
```

<details open>
<summary>Client</summary>

```python
from UdpSynchronous import UdpSynchronousClient

udp_client = UdpSynchronousClient("127.0.0.1", 20001, 1024) # create object from client class.

while(True):
    udp_client.write(['a', 'b', counter]) # you can sent your datas with "write" function.
```