'''1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais.
 Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.'''
import random
import string

senha = [] #litsa vazia apenas para ser preenchida posteriormente.
tam = 0 #variavel vazia para que o if a seguir possa funcionar.

#Laço que impede o usuário informar menos de 8 digitos
while True:
    tam = int(input('Informe o tamanho da senha, no mínimo 8 caracteres: '))
    if tam < 8:
        print('O tamanho mínimo são 8 caracteres!')
    else:
        break

#armazen de todos os caracteres (em variaveis para que facilitem o uso, poderiamos usar o def)
caracteres = string.ascii_uppercase + string.ascii_lowercase 
numeros = string.digits
simbolos = string.punctuation 


#sorteia 1 CARACTERE e salva na variavel senha, 'tam-2' será explicado a seguir
for c in range(tam - 2):
    sorteador = random.choice(caracteres)
    senha.append(sorteador)

#sorteia um numero e um simbolo, são apenas 2 para que assim tenhamos um mínimo de numero\simbolo.
senha = senha + [random.choice(numeros)] + [random.choice(simbolos)]

#embaralha tudo e printa para o usuario
random.shuffle(senha)
print(f'sua senha é: {''.join(senha)}')
