# [PT-BR] Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n1 = float(input('Value: '))

n2 = n1 - (n1 * 5 / 100)
print('{} with 5% off: {}'.format(n1, n2))
