'''3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
)'''
preco = float(input('Informe o preço original do produto: R$'))
desconto = float(input('Qual a porcentagem de desconto? %'))
porcentagem = desconto/100
preco_final = preco - (porcentagem * preco)
print(f'O preço final desse produto, já com desconto, foi de: R${preco_final:.2f}')