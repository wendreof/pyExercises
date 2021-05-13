# [PT-BR] Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

typed = str(input('What is your name again?: ')).strip()

conditional = 'Silva' in typed.title()

print('You are from Silva family?: {}.'.format(conditional))
