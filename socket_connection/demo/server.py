"""
create and open server side socket connection using tcp/ip protocol
"""

import socket

def run_server():
    """create a socket object"""
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 5555

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((server_ip, port))

    server.listen(0)
    print(f'Listening on {server_ip}: {port}')
    
    client_socket, client_adress = server.accept()
    print(f'accepted connection from {client_adress[0]}: {client_adress[1]}')

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break
        
        print(f"received: {request}")

        response = "accepted".encode("utf-8")
        try:
            client_socket.send(response)
        except Exception as e:
            print(e)
            break
            

    client_socket.close()
    print('Connection to client closed!')

    server.close()

run_server()

