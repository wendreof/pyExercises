# [PT-BR] Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
typed = int(input('Type some number from 0 to 9999: '))

unit = typed // 1 % 10
print('Unit: {}.'.format(unit))

ten = typed // 10 % 10
print('Ten: {}.'.format(ten))

hundred = typed // 100 % 10
print('Hundred: {}.'.format(hundred))

thousand = typed // 1000 % 10
print('Thousand: {}.'.format(thousand))
