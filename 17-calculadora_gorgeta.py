'''1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. 
Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.'''
print('Vamos calcular a sua gorgeta!')
while True:
    try:
        val_conta = float(input('Qual o valor da conta? R$'))
        gorgeta = float(input('Qual a porcentagem de gorgeta?'))
        resultado = val_conta * (gorgeta/100)
        break
    except ValueError:
        print('Digite apenas números!')

print(f'O valor da gorgeta é: R${resultado:.2f}')

      