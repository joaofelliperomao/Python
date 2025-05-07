def somar_pares():
    try:
        N = int(input("Digite um número inteiro positivo: "))
        if N < 1:
            print("Por favor, digite um número maior ou igual a 1.")
            return

       
        soma = sum(i for i in range(2, N + 1, 2))
        
        print(f"A soma dos números pares de 1 até {N} é: {soma}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")


somar_pares()
