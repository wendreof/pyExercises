# [PT-BR] Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from termcolor import colored

km = int(input('Type the Km/h of your car: '))

if km > 80:
    over = (km - 80)
    ticket = (over * 7)
    print(colored('Traffic ticket! You need to pay R$ {:.2f} cause the velocity.'.format(ticket), 'red'))
else:
    print(colored('Have a good one and keep driving safety!', 'blue'))
