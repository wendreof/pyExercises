# [PT-BR] Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

n1 = input('Type some number: ')
print('Is decimal? {} '.format(n1.isdecimal()))
print('Is space? {} '.format(n1.isspace()))
print('Is lower? {} '.format(n1.islower()))
print('Is isalnum? {} '.format(n1.isalnum()))
print('Is alpha? {} '.format(n1.isalpha()))
