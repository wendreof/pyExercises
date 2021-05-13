# [PT-BR] Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

name = str(input('Type your name: '))
name = name.rstrip().lstrip()

print('Your name in UppperCase: {}.'.format(name.upper()))
print('Your name in LowerCase: {}.'.format(name.lower()))
print('Your name has {} characters.'.format(len(name.replace(" ", ""))))

nameDiv = name.split()
print('Your 1st name is: {} and has {} characters.'.format(nameDiv[0].capitalize(), len(nameDiv[0])))

