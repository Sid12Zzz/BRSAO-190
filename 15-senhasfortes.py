'''3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  feito
* Verificar se a senha possui pelo menos 8 caracteres.  feito
* Verificar se contém pelo menos um número.  feito
* Informar se a senha é fraca ou forte.  feito
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair". feito  '''

qnt_num = []
senha = []
print('Vamos criar e analisar uma senha!')
print('Regra:\nUma senha forte tem no mínimo 8 caracteres e um número.')
print('Ao finalizar, escreva "sair" ')
while True:
        digito = input('Digite um caractere ou número: ').strip().upper()

        #Sair do loop
        if digito == 'SAIR':
            break

        #É numero?
        elif digito.isnumeric():
            qnt_num.append(+1)
            print('Registrado!')
            senha.append(digito)
            

        #É aplhanumerico (caso escreva a senha tudo junto)
        elif digito.isalnum():
              print('Registrado!')
              qnt_num.append(+1)
              senha.append(digito)

        #É caractere?
        elif digito.isalpha():
            print('Registrado!')
            senha.append(digito)

#senha final, toda junta
senha_final = ''.join(senha)
    
        
#Tem no minimo um numero? Se não, reescreva.

try:
    if qnt_num[0] > 0:
                print('Sua senha tem 1 número, boa!')
except IndexError:
      print('Sua senha não tem números! \nEla é fraca, escreva novamente.')

if len(senha_final) < 8:
      print('Sua senha não tem 8 caracteres!\n Ela é fraca, escreva novamente.')
else:
      print('Sua senha tem 8 caracteres, ela definitivamente é forte!')


print('Você quer ver a sua senha?')
s_n = input('[S] \ [N] ').strip().upper()
if s_n == 'S':
      print(f'Sua senha é: {senha_final}')
else:
      print('Ok, até mais!')
