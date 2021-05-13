# [PT-BR] Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
# pode comprar.

n1 = float(input('Type some value in R$: '))

n2 = n1 / 3.27
print('R$ {:.2f} = US$ {:.2f}'.format(n1, n2))

