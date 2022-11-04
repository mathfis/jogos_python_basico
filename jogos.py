import forca
import advinhacao
import jogo_da_velha

print('**********************************')
print('Escolha o seu jogo')
print('**********************************')

print("(1) Forca (2) Advinhação (3) Jogo da Velha")

jogo = int(input("Digite o número correspondente "))

if(jogo == 1):
    print("jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando Advinhação")
    advinhacao.jogar()
elif(jogo == 3):
    print("jogo da velha")
    jogo_da_velha.jogar()