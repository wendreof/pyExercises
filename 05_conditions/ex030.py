# [PT-BR] Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from termcolor import colored

number = int(input('Type some number: '))

if number % 2 == 0:
    print(colored('EVEN', 'green'))
else:
    print(colored('ODD', 'red'))
