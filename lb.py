import socket


def main():
    print("Starting")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket2:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket3:
                client_socket1.connect(('192.168.0.101', 80))
                client_socket2.connect(('192.168.0.102', 80))
                client_socket3.connect(('192.168.0.103', 80))
                with socket.socket() as server_socket:
                    server_socket.bind(('10.0.0.1', 80))
                    server_socket.listen(10)
                    while True:
                        connection_socket, connection_address = server_socket.accept()
                        print(connection_socket)
                        print(connection_address)
                        message = connection_socket.recv(1024)
                        print(message)
                        client_socket1.send(message)
                        answer = client_socket1.recv(1024)
                        print(answer)
                        connection_socket.send(answer)
                        connection_socket.close()


if __name__ == '__main__':
    main()



