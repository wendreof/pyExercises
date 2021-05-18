# [PT-BR]  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = int(input('Type the distance in km: '))

if distance <= 200:
    toPay = distance * 0.5
    print('Buss ticket value: R$ {:.2f}.'.format(toPay))
else:
    toPay = distance * 0.45
    print('Buss ticket value: R$ {:.2f}.'.format(toPay))
