'''2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"'''
peso = int(input('Digite seu peso (KG): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Seu peso está normal.')
else:
    print('Você está acima do peso.')