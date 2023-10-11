string = input("Digite uma palavra: ")
contador_vogais = 0

string = string.lower()
for char in string:
    if char in "aeiou":
        contador_vogais += 1
print("A quantidade de vogais na string é:", contador_vogais)

