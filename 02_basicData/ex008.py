# [PT-BR] Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = int(input('Type some number in Kilometers: '))

meters = (n1 * 1000)
centimeters = (n1 * 100000)
print('{} km in meters is: {}'.format(n1, meters))
print('{} km in meters is: {}'.format(n1, centimeters))
