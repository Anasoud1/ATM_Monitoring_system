"""
receiving electoric events data from the agent
"""

import socket
import tqdm
import os

seperator = "<>"

BUFFER_SIZE = 4096

host = ""
port = 5555

s = socket.socket()

s.bind((host, port))

s.listen(5)
print(f"[*] Listening as {host}:{port}")

client_socket, client_adress = s.accept()
print(f"[+] {client_adress[0]}:{client_adress[1]} is connected!")

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(seperator)

filename = os.path.basename(filename)
filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))
        

client_socket.close()
s.close()

with open("../data_received.txt", "w") as f:
    f.write("Data received")