# [PT-BR] Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Type n1: '))
n2 = int(input('Type n2: '))
n3 = int(input('Type n3: '))

if n1 > n2 and n1 > n3:
    print('BIGGEST == n1')
elif n2 > n1 and n2 > n3:
    print('BIGGEST == n2')
elif n3 > n1 and n3 > n2:
    print('BIGGEST == n3')

if n1 < n2 and n1 < n3:
    print('SMALLEST == n1')
elif n2 < n1 and n2 < n3:
    print('SMALLEST == n2')
elif n3 < n1 and n3 < n2:
    print('SMALLEST == n3')



