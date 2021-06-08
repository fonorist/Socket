def main():
    print("dssdfsf")
    try:
        with socket.socket() as server_socket:
            server_socket.bind(('10.0.0.1', 80))
            server_socket.listen(10)
            connection_socket, connection_address = server_socket.accept()
            print(connection_socket)
            print(connection_address)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as client_socket1:
                client_socket1.connect(('192.168.0.101', 80))
                message = connection_socket.recv(1024)
                print(message)
                client_socket1.send(message)
                answer = client_socket1.recv(1024)
                print(answer)
            connection_socket.send(answer)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    print('ebana rot')


if __name__ == '__main__':
    main()

