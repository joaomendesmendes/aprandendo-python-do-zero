"""agenda de contatos"""
print("Bem-vindo à sua agenda de contatos!")

"""Guardando os contatos"""
#dicionario vazio
agenda = {}

#adicionado os contatos e opçoes
print("preste atenção as opções do menu:")

while True:
    print("\n1. Adicionar contato")
    print("2. Busque contato")
    print("3.Sair")
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("nome:")
        tel = input("telefone:")
        agenda[nome] = tel
    elif opcao == "2":
         nome = input("nome para buscar:")
         if nome in agenda:
              print(f"telefone: {agenda[nome]}")
         else:
             print("contato não encontrado")
    elif opcao == "3":
         break
    
    