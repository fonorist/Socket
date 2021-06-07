import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect('192.168.0.101')


if __name__ == 'main':
    main()
