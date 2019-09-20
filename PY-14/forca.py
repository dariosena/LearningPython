import random

def jogar():
    imprime_messagem_de_abertura()
    
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        acertou = '_' not in letras_acertadas
        enforcou = erros == 7

        print(letras_acertadas)

    print()

    if (acertou):
        imprime_messagem_vencedor()
    else:
        imprime_messagem_perdedor(palavra_secreta)

    print()
    print('Fim do Jogo!')
    

def pede_chute():
    chute = input('\nQual letra? ')
    chute = chute.strip().upper()
    return chute

    
def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta
    
    
def imprime_messagem_de_abertura():
    print('************************************')
    print('***  Bem Vindo ao Jogo da Forca  ***')
    print('************************************')
    
def imprime_messagem_vencedor():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
    
def imprime_messagem_perdedor(palavra_secreta):
    print('Puxa, você foi enforcado!')
    print('A palavra era {}'.format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")
    