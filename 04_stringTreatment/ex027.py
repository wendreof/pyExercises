# [PT-BR] Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

typed = str(input('Type your full name: ')).strip().title()

div = typed.split()
last = len(div)-1

print('Your 1st name is: {}'.format(div[0]))
print('Your last name is: {}'.format(div[last]))
