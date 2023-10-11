def sequencia_fibonacci(n):
    fibonacci = [0, 1]

    if n <= 0:
        return "O número de termos deve ser maior que zero."
    elif n == 1:
        return [0]
    elif n == 2:
        return fibonacci

    while len(fibonacci) < n:
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)

    return fibonacci
num_termos = int(input("Digite o número de termos da sequência de Fibonacci: "))

resultado = sequencia_fibonacci(num_termos)
if isinstance(resultado, str):
    print(resultado)
else:
    print("Sequência de Fibonacci até", num_termos, "termos:", resultado)
