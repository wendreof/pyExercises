# [PT-BR] Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

typed = str(input('Type some phrase: ')).strip().lower()

div = typed.split()

print('Your phrase has {} \"a" characters.'.format(typed.count('a')))

print('1st founded in position {} of typed string'.format(typed.find('a')+1))

print('Last founded in position {} of typed string'.format(typed.rfind('a')+1))
