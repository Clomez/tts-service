from sys import argv, stdin

if len(argv) > 1:
    text = argv[1]
elif not stdin.isatty():
    text = stdin.read()
else:
    exit()

import socket

# Create the Unix socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    conn = client.connect(('localhost', 6060))
except FileNotFoundError:
    print('Server is offline')
    exit()

# Send a message to the server
client.send(text.encode())

# Close the connection
client.close()