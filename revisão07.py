def calcular_imc(peso, altura):
    if altura <= 0:
        return "A altura deve ser maior que zero."

    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))


imc = calcular_imc(peso, altura)
if isinstance(imc, str):
    print(imc)
else:
    print(f"O IMC é: {imc:.2f}")

