import random

# ------- BIBLIOTECA ---------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

def mensagem_erros(erros, erromax):
    print("\nVocê tem {} de {} erros".format(erros, erromax))
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        print("\n É A SUA ÚLTIMA CHANCE")
    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    cabecalho("Forca")
    palavra_secreta = carrega_palavra("palavras.txt")
    letras_acertadas = inicia_palavra(palavra_secreta)
    palavra_chute = palavra_lista(letras_acertadas)

    print('\nA palavra palavra secreta tem {} LETRAS.\n {}'.format(len(palavra_secreta), palavra_chute))

    enforcou = False
    acertou = False
    erros = 0
    erromax = 6

    # Enquanto True
    while (not enforcou and not acertou):
        mensagem_erros(erros, erromax)

        chute = carrega_letra()
        if chute in palavra_secreta:
            # escreve a lista de acertos
            letras_acertadas = compara_escreve(chute,palavra_secreta, letras_acertadas)
        else:
            erros +=1

        # Escreve a palavra_chute e imprime
        palavra_chute = palavra_lista(letras_acertadas)
        print(palavra_chute)

        # Atribui valores aos testes do while
        enforcou = erros == erromax+1
        acertou = palavra_chute == palavra_secreta

        # Termina o jogo por erros
        if enforcou:
            mensagem_forca(palavra_secreta, erros)

        # Termina o jogo por acertos
        if acertou:
            mensagem_vitoria_forca(palavra_secreta)
# ----------------------------------------------------------------------------------------------------

def cabecalho(nome_do_jogo):
    print('**********************************')
    print('Bem-vindo ao jogo de {}!'.format(nome_do_jogo))
    print('**********************************')
#
def carrega_palavra(nomearq, nlin=0, rand=True):
    #Carrega a palavra da linha nlin no arquivo nomearq
    #se rand == true, atribui valor aleatório para nlin
    #se rand == true, atribui valor aleatório para nlin

    # Abre o Arquivo de Leitura
    arquivo = open(nomearq, "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    if (rand == True):
        narq = len(palavras)
        nlin = random.randrange(0, narq)

    palavra = palavras[nlin].upper()
    return palavra

    # Fecha o arquivo de leitura
    arquivo.close()

# ----------------------------------------------------------------------------------------------------

def inicia_palavra(palavra):
    #Função que cria uma lista de subscritos do tamanho
    # de uma lista

    palavra_inicial = ["_" for letra in palavra]

    return palavra_inicial

# ----------------------------------------------------------------------------------------------------

def palavra_lista(lista):
    #Transforma uma lista de caracteres em uma palavra

    palavra = ''
    # Escreve uma palavra apenas de subescritos
    index = 0
    for letra in lista:
        palavra = palavra + lista[index]
        index = index + 1

    return palavra

# ----------------------------------------------------------------------------------------------------

def compara_escreve(letra_teste, palavra_original, palavra_copia):

# Verifica se 'letra_teste' é uma letra da lista 'palavra_original'
# identifica a posição onde se encontra e copia 'letra_teste'
# na posição correspondente da lista 'palavra_copia'

    index = 0
    for letra in palavra_original:
        if (letra_teste == letra):
            print("encontrei letra {} na posição {}".format(letra_teste, index))
            palavra_copia[index] = letra
        index = index + 1

    return palavra_copia

# ----------------------------------------------------------------------------------------------------

def carrega_letra():
    letra = str(input("Escolha uma letra: "))
    letra = letra.strip().upper()

    return letra

# ----------------------------------------------------------------------------------------------------

def mensagem_forca(palavra_secreta,erros=7):
    print('\nVocê atingiu {} erros. Fim de Jogo!'.format(erros))
    print("VOCÊ FOI ENFORCADO!")
    print("A palavra era {}".format(palavra_secreta))
    print("\n")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

# ----------------------------------------------------------------------------------------------------

def mensagem_vitoria_forca(palavra_secreta):
    print("\nVocê acertou! A palavra secreta é {}!".format(palavra_secreta))
    print("Parabéns, você ganhou!")
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

# ----------------------------------------------------------------------------------------------------
# --FIM DA BIBLIOTECA --------------------------------------------------------------------------------

# Chama a Main
if (__name__ == "__main__"):
    jogar()
