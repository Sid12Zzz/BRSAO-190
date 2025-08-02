'''2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.  '''

'''colocando itens dentro da lista'''
from time import sleep

while True:
    lista = []
    try:
        #Cabeçalho do programa
        print('Vamos calcular a média dos seus alunos!')
        sleep(1)
        print('Digite as notas e ao terminar, digite "fim"')
        sleep(1)
        print('**Não serão aceitos números por extenso e notas acima de 10!')

        '''Coletando inputs, armazenando e transformando no tipo 
            certo e finalizando o laço'''
        for c in range (0,1000):
            numeros = (input('Digite os números: ').upper().strip())
            if numeros == "FIM":
                break
            numeros_float = float(numeros)
            lista.append(numeros_float)


        '''Permitindo apenas numeros abaixo de 10 e calculando a media'''
        if max(lista) > 10:
            print('Siga as instruções!! \n (Apenas números entre 0 e 10)')
        else:
            media = sum(lista) / len(lista)
            print(f'As notas informadas foram: {lista}')
            print(f'A média dos alunos foi de: {media:.2f}')
            break

        #Casos de erro
    except ValueError:
        print('Siga as instruções!!')
        print('Sem números por extenso e textos!')
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')