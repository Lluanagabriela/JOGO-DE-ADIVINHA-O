import forca 
import jogoadivinhacao
    
print('**********************************')
print('********Escolha seu jogo!*********')
print('**********************************')

print ('(1) Forca (2) Adivinhação')

jogo = int(input ('Qual jogo você quer jogar?'))

if(jogo == 1):
    print('Jogando jogo da Forca')
    forca.jogar_forca()
else:
    print('Jogando jogo da Adivinhação')
    jogoadivinhacao.jogar_adivinhacao()