def sao_anagramas(frase1, frase2):

    limpa1 = ''.join(c.lower() for c in frase1 if c.isalnum())
    limpa2 = ''.join(c.lower() for c in frase2 if c.isalnum())


    return sorted(limpa1) == sorted(limpa2)


texto1 = input("Digite a primeira palavra ou frase: ")
texto2 = input("Digite a segunda palavra ou frase: ")


if sao_anagramas(texto1, texto2):
    print(" As frases são anagramas!")
else:
    print(" As frases não são anagramas.")
