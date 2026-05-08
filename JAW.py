"""Jogo de adivinhação com while - Versão melhorada"""

import random

def obter_numero_valido():
    """Pede um número válido entre 1 e 10"""
    while True:
        try:
            num = int(input("Adivinhe um número entre 1 e 10: "))
            if 1 <= num <= 10:
                return num
            else:
                print("Por favor, digite um número entre 1 e 10!")
        except ValueError:
            print("Por favor, digite um número válido!")

def jogar():
    """Função principal do jogo"""
    numero_secreto = random.randint(1, 10)
    nome = input("Qual é o seu nome? ")
    print(f"Bem-vindo ao jogo de adivinhação, {nome}!")
    print("Você precisa acertar um número entre 1 e 10!\n")
    
    tentativas = 0
    
    while True:
        usuario = obter_numero_valido()
        tentativas += 1
        
        if usuario == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif usuario < numero_secreto:
            print("❄️ Tá frio! O número é MAIOR!\n")
        else:
            print("🔥 Tá quente! O número é MENOR!\n")

# Executa o jogo
jogar()