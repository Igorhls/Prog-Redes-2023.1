import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        data, _ = client_socket.recvfrom(4096)
        message = data.decode()
        print(message)

def send_messages(client_socket):
    while True:
        message = input("Digite uma mensagem (ou 'sair' para encerrar): ")

        if message == 'sair':
            client_socket.close()
            break

        if len(message.encode()) > 64:
            print("A mensagem excede o limite de 64 bytes.")
            continue

        client_socket.sendto(message.encode(), (server_ip, 5000))

def start_client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client_socket.bind(('0.0.0.0', 0))

    print("Cliente conectado ao servidor.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

if __name__ == '__main__':
    server_ip = input("Digite o endereço IP do servidor (ou pressione Enter para usar o IP local): ")
    if not server_ip:
        server_ip = socket.gethostbyname(socket.gethostname())
    start_client(server_ip)
