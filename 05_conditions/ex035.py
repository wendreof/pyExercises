# [PT-BR] Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

r1 = float(input('Type 1st length: '))
r2 = float(input('Type 2nd length: '))
r3 = float(input('length 3rd length: '))

sit_1 = ((r2 - r3) < r1 < (r2 + r3))
sit_2 = ((r1 - r3) < r2 < (r1 + r3))
sit_3 = ((r1 - r2) < r3 < (r1 + r2))

if sit_1 and sit_2 and sit_3:
    print('Yes it is possible')
else:
    print('Crap! Its not possible...')
