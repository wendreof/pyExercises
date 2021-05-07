# [PT-BR] Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

students = []

for item in range(4):
    a = str(input('Type the student number {}: '.format(item+1)))
    students.append(a)

choice = choice(students)

print('The result is: {}.'.format(choice))
