km = float(input('Qual a quantidade de km pecorrida? '))
dias = float(input('Qual a quantidade de dias pecorrida? '))
valor = (km * 0.15) + (dias * 60)
print('O preço que voce pagará é de R${:.2f}'.format(valor))