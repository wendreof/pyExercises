# [PT-BR] Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

n1 = int(input('Type some number: '))
double = n1 * 2
triple = n1 * 3
squareRoot = math.sqrt(n1)
print('Typed: {} \nDouble is 2: {} \nTriple is: {} \nsquareRoot is: {} '.format(n1, double, triple, squareRoot))
