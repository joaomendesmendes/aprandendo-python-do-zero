"""compras do mes"""
#criando uma lista vazia
compras = []

"""itens da lista de compras"""
item1 = input("Digite o primeiro item da lista de compras: ")
item2 = input("Digite o segundo item da lista de compras: ")
item3 = input("Digite o terceiro item da lista de compras: ")

#adicionando os itens à lista de compras
compras.append(item1)
compras.append(item2)
compras.append(item3)

#Loop (while) para perguntar se o usuário deseja adicionar mais itens à lista de compras
while True:
    resposta = input("Deseja adicionar mais itens à lista de compras? (s/n): ")
    if resposta.lower() == 's':
        item = input("Digite o próximo item da lista de compras: ")
        compras.append(item)
    elif resposta.lower() == 'n':
       print("Lista de compras finalizada,fim.")
       break
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
        
"""Exibindo a lista de compras"""
print("Sua lista de compras é:")
for item in compras:
    print("- " + item)

"""total de itens na lista de compras"""
itens_total = len(compras)
print("Total de itens na lista de compras:", itens_total)








































