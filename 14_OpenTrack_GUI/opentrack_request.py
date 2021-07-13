import requests
import socket
import threading

PORT = 9005
ot_receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ot_receiver.bind((socket.gethostname(), PORT))
ot_receiver.listen(1)


def connect_ot():
    #threading.Thread(target=rest_on_port).start()
    return True


# ------------------------- Network Socket -------------------------
def ot_buffer(msg):
    print(msg)
    print(40 * "--")


def rest_on_port():
    while True:
        conn, addr = ot_receiver.accept()
        print(f"Connected to {addr}")

        while True:
            data = conn.recv(512).decode("utf-8")

            if data:
                threading.Thread(target=ot_buffer, args=(data,)).start()
            else:
                print("received ")
                break

            if data == 0:
                conn.close()