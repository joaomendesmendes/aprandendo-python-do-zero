"""calculadora de Dia da Semana"""
print("Digite um número de 1 a 7 para saber o dia da semana correspondente: ")
dia = int(input())

"""dias da semana"""
match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido")
  