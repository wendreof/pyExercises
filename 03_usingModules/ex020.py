# [PT-BR] O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

students = []

for item in range(4):
    a = str(input('Type the student number {}: '.format(item+1)))
    students.append(a)

shuffle(students)

print('The result is: {}.'.format(students))
