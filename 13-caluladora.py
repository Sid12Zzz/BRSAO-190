'''1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.'''
from time import sleep
while True:

    try:
        n1 = float(input('Digite um primeiro número:'))
        print('Qual o operador?')
        operador = str(input('[+] [-] [/] [*]'))
        n2 = float(input('Digite outro número: '))


        if operador == '+':
            resultado = n1 + n2
        elif operador == '-':
            resultado = n1 - n2
        elif operador == '/':
            resultado = n1 / n2
        elif operador == '*':
            resultado = n1 * n2
        else:
            print('O operador está errado! vamos novamente')
            continue
        print(resultado)
        break

    except ZeroDivisionError:
        print('Erro: Não é possível divir por zero!')
        print('Vamos tentar novamente!')
    except ValueError:
        print('Erro: Digite apenas números!')
        print('Vamos tentar novamente!')
    except TypeError:
        print('Erro: Cálculos apenas com: int & float.')
        print('Vamos tentar novamente!')
    