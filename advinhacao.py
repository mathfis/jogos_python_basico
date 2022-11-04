def jogar():

    import random

    print('**********************************')
    print('Bem-vindo ao jogo de Advinhação!')
    print('**********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    facil = nivel == 1
    medio = nivel == 2
    dificil = nivel == 3
    nivel_valido = facil or medio or dificil

    # introduzir o nível e admitir apenas respostas válidas
    while(total_de_tentativas == 0):
        if(nivel_valido):
            if(facil):
                total_de_tentativas = 20
            elif(medio):
                total_de_tentativas = 10
            elif(dificil):
                total_de_tentativas = 5
        else:
            print("Você deve digitar os números 1, 2 ou 3.")
            print("")
            print("Qual o nível de dificuldade?")
            print("(1) Fácil (2) Médio (3) Difícil")
            nivel = int(input("Defina o nível: "))

            facil = nivel == 1
            medio = nivel == 2
            dificil = nivel == 3
            nivel_valido = (facil)or(medio)or(dificil)

    for rodada in range(1,total_de_tentativas+1):

        print('\ntentativa', rodada, 'de', total_de_tentativas) #no python, o for é exclusivo
        chute_str = input('Digite um Número entre 1 e 100\n')
        print('você digitou ', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('você deve digitar entre 1 e 100!')
            continue #vai para a iteração seguinte

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if acertou: #estrutura sem parênteses permitida
            print('Você acertou! Marcou {} pontos'.format(pontos))
            break #abandona o laço
        else:
            print('Você errou!', end=' ')
            if(menor):
                print('O número digitado é MENOR que o número secreto\n')
            elif(maior):
                print('O número digitado é MAIOR que o número secreto\n')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(rodada == total_de_tentativas):
                print('O seu número de tentativas se esgotou.\n')
                print('O número secreto é', numero_secreto)
                print('Você marcou {} pontos'.format(pontos))

        rodada = rodada + 1

    print('Fim', 'do', 'jogo!',sep=' ')

if(__name__ == "__main__"):
    jogar()