## udp-server.py
```bash
> python3 udp-server.py
starting up on ./udp_socket_file

waiting to receive message...
received 11 bytes from ./udp_client_socket_file
b'HelloWorld!'
sent 14 bytes back to ./udp_client_socket_file

waiting to receive message...
```

## udp-client.py
```bash
> python3 udp-client.py HelloWorld!
sending b'HelloWorld!'
waiting to receive...
received b'Pamela Manning'
closing socket
```
