import socket
import threading

clientes = {}

def handle_client(client_socket, client_address):
    while True:
        try:
            data, _ = client_socket.recvfrom(4096)
            message = data.decode()

            if not message.strip():
                continue

            clientes[client_address] = True

            for address in clientes.keys():
                if address != client_address:
                    client_socket.sendto(f'{client_address}: {message}'.encode(), address)

        except Exception as e:
            print(f"Erro na conexão com o cliente {client_address}: {str(e)}")
            break

def start_server(server_ip):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, 5000))

    print("Servidor de chat iniciado.")
    print(f"O servidor está ouvindo em {server_ip}:5000.")

    while True:
        data, address = server_socket.recvfrom(64)

        client_thread = threading.Thread(target=handle_client, args=(server_socket, address))
        client_thread.start()

if __name__ == '__main__':
    server_ip = input("Digite o endereço IP do servidor (ou pressione Enter para usar todas as interfaces locais): ")
    if not server_ip:
        server_ip = '0.0.0.0'
    start_server(server_ip)
