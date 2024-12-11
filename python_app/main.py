import socket

SERVERHOST = '0.0.0.0'
SERVERPORT = 8000

def runtcpserver():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"Servidor TCP en {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión entrante de {client_address}")
        client_socket.send(b"Bienvenido al servidor TCP")
        client_socket.close()

if __name == '__main':
    run_tcp_server()
