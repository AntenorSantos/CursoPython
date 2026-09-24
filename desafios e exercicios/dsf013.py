s = float(input('Qual o salario de um funcionario? R$'))
a = s + (s * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com o aumento de 15%, começou a ganhar R${:.2f}'.format(s,a))