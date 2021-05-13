# [PT-BR] Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Type some number: '))

for item in range(n1+1):
    print('{0} * {1} = {2} '.format(n1, item, n1*item))
