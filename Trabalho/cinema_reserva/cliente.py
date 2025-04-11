import socket

def iniciar_cliente(host='127.0.0.1', porta=12345):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    print(cliente.recv(1024).decode())

    while True:
        comando = input("Digite comando (VER, RESERVAR 1 2 3, SAIR): ")
        cliente.sendall(comando.encode())

        resposta = cliente.recv(4096).decode()
        print(f"Resposta:\n{resposta}")

        if comando.strip().upper() == "SAIR":
            break

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()
