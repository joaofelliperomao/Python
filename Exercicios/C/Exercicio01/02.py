def separar_digitos():
    numero = input("Digite um número de 5 dígitos: ")

    if len(numero) != 5 or not numero.isdigit():
        print("Entrada inválida. Certifique-se de digitar exatamente 5 dígitos.")
        return

    digitos_separados = '   '.join(numero)
    print("Dígitos separados:")
    print(digitos_separados)

separar_digitos()
