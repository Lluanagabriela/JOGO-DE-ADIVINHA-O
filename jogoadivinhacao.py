#jogoadivinhacao
print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 22

#Definindoo 0 número de tentativas
numeroTentativas = 3

while (numeroTentativas > 0):

    chuteString = input ('Digite um número ')

    print('Você digitou um número')

    chute = int(chuteString)

    if numeroSecreto == chute:  
        print ('VOCÊ ACERTOU!')
    elif(chute>numeroSecreto):
        print('Você errou! O número secreto é menor!')
    else:
        print('Você errou! O número secreto é maior!')


