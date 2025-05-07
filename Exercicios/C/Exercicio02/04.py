import string

def eh_palindromo(frase):

    frase_limpa = ''.join(
        c.lower() for c in frase if c.isalnum()
    )

    return frase_limpa == frase_limpa[::-1]


texto = input("Digite uma frase para verificar se é um palíndromo: ")


if eh_palindromo(texto):
    print(" É um palíndromo!")
else:
    print(" Não é um palíndromo.")
