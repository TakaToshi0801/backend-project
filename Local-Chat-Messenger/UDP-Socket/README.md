## udp-server.py
```bash
> python3 udp-server.py
starting up on /home/test/mydir/recursion/Local-Chat-Messenger/UDP-Socket/udp_socket_file

waiting to receive message...
received 11 bytes from /home/test/mydir/recursion/Local-Chat-Messenger/UDP-Socket/udp_client_socket_file
b'HelloWorld!'
sent 14 bytes back to /home/test/mydir/recursion/Local-Chat-Messenger/UDP-Socket/udp_client_socket_file

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