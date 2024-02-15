print ('**********************************')
print ('Bem vindo, ao  JOGO DE ADIVINHAÇÃO')
print ('**********************************')

numeroSecreto = 16

chute = input('digite um número')

print ('você digitou o número', chute)

if numeroSecreto == chute : 
    print ('Você acertou!')

else :
    print('Você errou!')