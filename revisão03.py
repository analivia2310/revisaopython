import string
def e_palindromo(frase):
    frase = frase.lower()
    frase = ''.join(c for c in frase if c not in string.punctuation and c != ' ')
    return frase == frase[::-1]
entrada = input("Digite uma palavra ou frase: ")
if e_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
