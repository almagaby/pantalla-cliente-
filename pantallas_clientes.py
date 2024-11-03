import socket
import cv2
import numpy as np
import struct
from PIL import ImageGrab

def capture_and_send_screen(conn):
    while True:
        screen = np.array(ImageGrab.grab())
        _, frame = cv2.imencode('.jpg', screen)
        data = frame.tobytes()
        msg_size = struct.pack(">L", len(data))
        conn.sendall(msg_size + data)

def client_program():
    host = '172.168.2.244'
    port = 5001  # Usa el mismo puerto que en el servidor
    client_socket = socket.socket()
    client_socket.connect((host, port))
    capture_and_send_screen(client_socket)
    client_socket.close()

if __name__ == '__main__':
    client_program()
