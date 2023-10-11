# Solicita ao usuário para inserir as cinco notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3 ) / 3
if media >= 7:
    print("O aluno foi aprovado com média", media)
else:
    print("O aluno foi reprovado com média", media)
