import socket


def main():
    with socket.socket() as server_sock:
        server_sock.bind(('10.0.0.0', 80))
        server_sock.listen(5)
        connection_socket, connection_address = server_sock.accept()
        b = connection_socket.recv(1024)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
            client_sock.connect(('192.168.0.101', 80))
            message = b
            client_sock.send(message)
            received_message = client_sock.recv(1024)
            connection_socket.send(received_message)


if __name__ == 'main':
    main()
