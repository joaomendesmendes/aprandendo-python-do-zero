"""nome do aluno(a)"""
nome= input("Digite o nome de aluno(a):")
print("O nome do aluno(a) é:", nome)

"""boletim de notas do aluno(a)"""
print("Digite a primeira nota: ")
nota1 = float(input())

print("Digite a segunda nota: ")
nota2 = float(input())

print("Digite a terceira nota: ")
nota3 = float(input())

"""formula para calcular a média"""
media = (nota1 + nota2 + nota3) / 3

"""situação final do aluno(a)"""
print("A média do aluno(a) é:", media)

"""tabela de ref da média""" 
if media >=5 and media < 7:
    print("Situação final: Recuperação")
elif media >= 7:
    print("Situação final: Aprovado")   
elif media < 5:
    print("Situação final: Reprovado")  