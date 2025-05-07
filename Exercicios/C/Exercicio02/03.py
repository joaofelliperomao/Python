def desenhar_quadrado():
    try:
        lado = int(input("Digite o tamanho do lado do quadrado (1 a 20): "))
        
        if lado < 1 or lado > 20:
            print("Tamanho inválido. O valor deve estar entre 1 e 20.")
            return

        for linha in range(lado):
            if linha == 0 or linha == lado - 1:
                print('*' * lado) 
            else:
                print('*' + ' ' * (lado - 2) + '*') 

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")


desenhar_quadrado()
