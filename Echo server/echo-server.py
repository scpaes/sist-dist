import socket
import sys
from datetime import datetime

def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 8189))
    connection.listen(10)
    server_time = str(datetime.now()).encode()
    server_system = sys.version.encode()
    while True:
        current_connection, address = connection.accept()
        while True:
            start_message = 'Hello, Enter BYE to exit type: 1 server hour or type: 2 server-version'
            start_message = start_message.encode()
            current_connection.send(start_message)
            data = current_connection.recv(2048)
            if data == 'BYE\r\n'.encode():
                current_connection.shutdown(1)
                current_connection.close()
            elif data == '1\r\n'.encode() or data == '1'.encode():
                current_connection.send(server_time)
            elif data == '2\r\n'.encode() or data == '2'.encode():
                current_connection.send(server_system)
            elif data:
                current_connection.send(data)
                print(data)


if __name__ == "__main__":

    try:
        listen()
    except KeyboardInterrupt:
        pass
