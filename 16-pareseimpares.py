'''4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  '''

#Cabeçalho   
print('Vamos analisar seus números!')
print('Digite números inteiros, e no final digite "fim" ')

par = []
impar = []
while True:
    try:
        #Listas + input + checagem fim + transformação
        numero = input('Digite um número inteiro: ').upper().strip()
        if numero == 'FIM':
            print('Você encerrou o código!')
            break
        numero_int = int(numero)

        #Condição para saber se é par ou ímpar ou sair
        if numero_int % 2 == 0:
            print('Este número é par!')
            par.append(numero_int)
        else:
            print('Este número é impar!')
            impar.append(numero_int)
    except ValueError:
        print('Digite apenas números!')
    
print(f'Você informou {len(par)} números pares, eles são: \n {par}')
print(f'Você informou {len(impar)} números impares, eles são: \n {impar}')

