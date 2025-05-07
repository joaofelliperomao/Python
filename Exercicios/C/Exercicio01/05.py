def criptografar(numero):
    if len(numero) != 4 or not numero.isdigit():
        return "Erro: Digite exatamente 4 dígitos."

   
    digitos = [(int(d) + 7) % 10 for d in numero]


    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

  
    criptografado = ''.join(map(str, digitos))
    return criptografado


entrada = input("Digite um número de 4 dígitos para criptografar: ")
resultado = criptografar(entrada)
print(f"Número criptografado: {resultado}")

def descriptografar(numero):
    if len(numero) != 4 or not numero.isdigit():
        return "Erro: Digite exatamente 4 dígitos."

 
    digitos = [int(d) for d in numero]


    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

 
    original = [(d - 7 + 10) % 10 for d in digitos]

    return ''.join(map(str, original))


entrada = input("Digite um número criptografado de 4 dígitos para descriptografar: ")
resultado = descriptografar(entrada)
print(f"Número original: {resultado}")
