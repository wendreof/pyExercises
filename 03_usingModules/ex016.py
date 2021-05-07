# [PT-BR] Crie um programa que leia um nº Real qualquer pelo teclado e mostre na tela sua porção inteira.
num = float(input('Type some number: '))

print('You have typed: {0}.\n'
      'Casting to integer is: {1}.'.format(num, int(num)))
