import socket
import threading

# Inicializa os assentos (todos disponíveis no início)
assentos = [False] * 100  # False = disponível, True = reservado
lock = threading.Lock()

def tratar_cliente(conexao, endereco):
    print(f"[+] Conexão estabelecida com {endereco}")
    conexao.sendall(b"Bem-vindo ao sistema de reservas do cinema!\n")

    while True:
        try:
            dados = conexao.recv(1024).decode().strip()
            if not dados:
                break

            print(f"[{endereco}] Requisicao: {dados}")

            if dados == "VER":
                with lock:
                    estado = ''.join(['X' if x else '_' for x in assentos])
                conexao.sendall(estado.encode())

            elif dados.startswith("RESERVAR"):
                _, *indices = dados.split()
                indices = list(map(int, indices))
                resultado = []

                with lock:
                    for i in indices:
                        if 1 <= i <= 100:
                            if not assentos[i - 1]:
                                assentos[i - 1] = True
                                resultado.append(f"Assento {i}: OK")
                                print(f"[RESERVADO] Cliente {endereco} reservou assento {i}")
                            else:
                                resultado.append(f"Assento {i}: Indisponível")
                        else:
                            resultado.append(f"Assento {i}: Inválido")

                conexao.sendall('\n'.join(resultado).encode())

            elif dados == "SAIR":
                conexao.sendall(b"Conexao encerrada.\n")
                break
            else:
                conexao.sendall(b"Comando invalido. Use VER, RESERVAR <num>, SAIR.\n")

        except Exception as e:
            print(f"[ERRO] Erro com cliente {endereco}: {e}")
            break

    conexao.close()
    print(f"[-] Conexão encerrada com {endereco}")

def iniciar_servidor(host='127.0.0.1', porta=12345):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()

    print(f"[SERVIDOR] Rodando em {host}:{porta}")

    while True:
        conexao, endereco = servidor.accept()
        threading.Thread(target=tratar_cliente, args=(conexao, endereco), daemon=True).start()

if __name__ == "__main__":
    iniciar_servidor()
