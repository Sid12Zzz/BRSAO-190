nome_produto = "camiseta"
preco_original = 50
desconto = 20/100
preco_final = preco_original * desconto
print(f'Você comprou o produto: {nome_produto}')
print(f'Seu preço original era: {preco_original:.2f}')
print(f'Com R${desconto * 100} ele custará: {preco_final}')