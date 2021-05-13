# [PT-BR] Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n1 = float(input('Type your salary: '))
newSalary = n1 + (n1 * 0.15)
print('Congrats, your earned 15% increase this month. \nYour new salary is: {:.2f} '.format(newSalary))
