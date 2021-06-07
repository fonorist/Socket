import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket:
        client_socket.connect(('192.168.0.102', 80))
        message_to_send = 'M1'
        client_socket.send(message_to_send.encode())


if __name__ == 'main':
    main()
