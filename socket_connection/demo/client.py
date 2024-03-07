"""
create and connect client side socket to server
"""

import socket

def run_client():
    """
    create a client socket object
    """

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = '100.25.15.47'
    port = 5555

    client.connect((server_ip, port))
    try:
        while True:
            
            msg = input("Enter message: ")
            client.send(msg.encode('utf-8')[:1024])

            respond = client.recv(1024)
            respond = respond.decode('utf-8')

            if respond.lower() == "closed":
                break
            
            print(f'recerved: {respond}')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print('connedtion to server closed!')

run_client()
