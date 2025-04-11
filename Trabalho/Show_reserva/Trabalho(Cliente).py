import socket

def conectar_ao_servidor():
    
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(("127.0.0.1", 12345))

    # Solicita assentos
    assentos = input("Digite os números dos assentos a serem reservados, separados por vírgula: ")
    
    # Envia os dados ao servidor
    cliente_socket.send(assentos.encode("utf-8"))

    # Recebe a resposta do servidor
    resposta = cliente_socket.recv(1024).decode("utf-8")
    print("Resposta do servidor:", resposta)

    cliente_socket.close()

if __name__ == "__main__":
    conectar_ao_servidor()
