"""info do usuário"""
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))


"""calculo do IMC"""
IMC = peso / (altura ** 2)


"""tabela de ref do IMC"""
if IMC < 18.5: 
    print("Abaixo do peso")

elif 18.5 <= IMC < 25:
    print("peso normal")    

elif 25 <= IMC < 30:
    print("sobrepeso")

elif IMC >= 30:
    print("obesidade")


"""imprime o resultado do IMC"""
print ("O valor do IMC é:", IMC)
