import socket
import threading

# Número de assentos no cinema
NUM_ASSENTOS = 100

# Lista para armazenar a disponibilidade dos assentos
assentos = [True] * NUM_ASSENTOS  # True significa disponível, False significa reservado

# Mutex para controlar o acesso aos assentos
mutex = threading.Lock()

def reservar_assento(cliente_socket, cliente_endereco):
    try:
        # Recebe a solicitação do cliente (número do assento ou assentos)
        dados = cliente_socket.recv(1024).decode("utf-8")
        assentos_solicitados = list(map(int, dados.split(',')))

        with mutex:  # Garante exclusão mútua (mutex)
            print(f"Cliente {cliente_endereco} solicitou os assentos {assentos_solicitados}")

            # Verifica se todos os assentos solicitados estão disponíveis
            for assento in assentos_solicitados:    
                if assentos[assento - 1] == False:
                    cliente_socket.send("Erro: Um ou mais assentos já estão reservados.".encode())
                    print(f"Cliente {cliente_endereco} falhou ao tentar reservar os assentos {assentos_solicitados}")
                    return
            
            # Reserva os assentos
            for assento in assentos_solicitados:
                assentos[assento - 1] = False

            cliente_socket.send("Reserva bem-sucedida!".encode())
            print(f"Cliente {cliente_endereco} reservou os assentos {assentos_solicitados}")
    except Exception as e:
        print(f"Erro ao processar a solicitação de {cliente_endereco}: {e}")
    finally:
        cliente_socket.close()

def iniciar_servidor():
    # Configuração do servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(("127.0.0.1", 12345))  
    servidor_socket.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        cliente_socket, cliente_endereco = servidor_socket.accept()
        print(f"Conexão recebida de {cliente_endereco}")
        
        # Cria uma nova thread para lidar com o cliente
        threading.Thread(target=reservar_assento, args=(cliente_socket, cliente_endereco)).start()

if __name__ == "__main__":
    iniciar_servidor()
