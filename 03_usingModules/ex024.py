# [PT-BR] Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
typed = str(input('What is your city?: ')).strip()

conditional = typed.capitalize().startswith('Santo')

print('Your city name starts with word \'Santo\'?: {}.'.format(conditional))
