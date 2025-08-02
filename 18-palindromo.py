'''2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, 
ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, 
acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.'''

palavra = (input('Digite uma palavra, veremos se é um palindromo.').strip().upper().split())
palavra_utilizavel = ''.join(palavra)
palindromo = palavra_utilizavel[::-1]
if palindromo == palavra_utilizavel[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palindromo!')
