"""
sending atm ecletronic events flat file data to the ATM handler
"""

import socket
import tqdm
import os

seperator = "<>"

BUFFER_SIZE = 4096

host = "100.25.15.47"
port = 5555

filename = "events.json"
filesize = os.path.getsize(filename)

s = socket.socket()
print(f"Connecting to {host}:{port}")

s.connect((host, port))
print("[+] Connected.")

s.send(f"{filename}{seperator}{filesize}".encode("utf-8"))

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break

        s.sendall(bytes_read)

        progress.update(len(bytes_read))

s.close()
