import socket


def main():
    print("dssdfsf")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket1:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket2:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket3:
                    client_socket1.connect(('192.168.0.101', 80))
                    client_socket2.connect(('192.168.0.102', 80))
                    client_socket3.connect(('192.168.0.103', 80))
                    with socket.socket() as server_socket:
                        server_socket.bind(('10.0.0.0', 80))
                        server_socket(5)
                        connection_socket, connection_address = server_socket.accept()
                        message = connection_socket.recv(1024)
                        client_socket1.send(message)
                        answer = client_socket1.recv(1024)
                        server_socket.send(answer)
                    #message_to_send = 'M1'
                    #client_socket1.send(message_to_send.encode())
    except Exception as error:
        print(error)

    print('ebana rot')


if __name__ == '__main__':
    main()
