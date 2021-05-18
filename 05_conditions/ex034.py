# [PT-BR] Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

oldSalary = float(input('Type your salary: '))

if oldSalary > 1250:
    newSalary = oldSalary + (oldSalary * 0.10)
    print('Congrats, your earned 10% increase this month. \nYour new salary is: {:.2f} '.format(newSalary))
elif (oldSalary <= 1250) and (oldSalary > 0):
    newSalary = oldSalary + (oldSalary * 0.15)
    print('Congrats, your earned 15% increase this month. \nYour new salary is: {:.2f} '.format(newSalary))
else:
    print('Your salary will be the same this month!')
