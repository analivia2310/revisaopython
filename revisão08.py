def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

escolha = input("Escolha a conversão (C para Celsius para Fahrenheit, F para Fahrenheit para Celsius): ")

if escolha == "C" or escolha == "c":
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit.")
elif escolha == "F" or escolha == "f":
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.2f} graus Celsius.")
else:
    print("Escolha inválida. Por favor, escolha C ou F.")
