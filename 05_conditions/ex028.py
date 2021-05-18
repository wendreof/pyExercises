# [PT-BR] Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

from random import randint
from time import sleep

number = randint(0, 5)
typed = int(input('Type some number between 0-5: '))

print('Analysing...')
sleep(2)

print('Number chosen was {}.'.format(number))
if typed == number:
    print('Congrats. You rock!!')
else:
    print('Please, try again!!')
