import socket


def main():
    print("dssdfsf")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket:
        try:
            client_socket.connect(('192.168.0.102', 80))
            message_to_send = 'M1'
            client_socket.send(message_to_send.encode())
        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()
