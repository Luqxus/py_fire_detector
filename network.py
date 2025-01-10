import time
import socket
import json


HOST = "13.247.60.143"
PORT = 80

deviceID = "1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(1.0)
addr = (HOST, PORT)

def send_temperature(value):
    data = json.dumps({"device_id": deviceID, "key": "temperature", "value": value})
    print(data)
    client_socket.sendto(bytes(data, "utf-8"), addr)

    

def call_server(confidence: int):
    if confidence > 50:
        print("confidence : ", confidence)
        # print("confidence : in bytes", bytes(confidence))
        time.sleep(0.3)
        
        data = json.dumps({"device_id": deviceID, "key": "fire", "value": confidence})
        print(data)
        
        # start = time.time()
        client_socket.sendto(bytes(data, "utf-8"), addr)

# while True:
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # client_socket.settimeout(1.0)
#     message = b'network test'
#     addr = ("127.0.0.1", 3000)

#     # start = time.time()
#     client_socket.sendto(message, addr)
#     # try:
#     #     data, server = client_socket.recvfrom(1024)
#     #     # end = time.time()
#     #     # elapsed = end - start
#     #     # print(f'{data} {pings} {elapsed}')
#     # except socket.timeout:
#     #     print('REQUEST TIMED OUT')