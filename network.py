import time
import socket



HOST = "13.247.60.143"
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(1.0)
addr = (HOST, PORT)

def send_temperature(value):
    client_socket.sendto(value.to_bytes(2, 'little'), addr)

    

def call_server(confidence: int):
    if confidence > 50:
        print("confidence : ", confidence)
        # print("confidence : in bytes", bytes(confidence))
        time.sleep(0.3)
        
        # start = time.time()
        client_socket.sendto(confidence.to_bytes(2, 'little'), addr)

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