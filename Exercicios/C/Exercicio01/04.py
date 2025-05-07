def contar_vogais():
    frase = input("Digite uma frase: ")
    
 
    frase = frase.lower()
    

    vogais = "aeiou"
    

    total_vogais = sum(1 for letra in frase if letra in vogais)
    
    print(f"\nA frase contém {total_vogais} vogais.")


contar_vogais()
