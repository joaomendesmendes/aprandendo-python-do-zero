contador = 0
while contador < 5:
    print(contador)
    contador += 1

#while com Flag
ativo = True
while ativo:
    resposta= input("quer continuar? (s/n): ")
    if resposta=="n":
        ativo = False
        print("Programa encerrado.")
