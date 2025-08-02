# 1. Importar o módulo necessário para trabalhar com arquivos CSV
import csv

# 2. Criar uma lista de listas com os dados fictícios
#    É uma boa prática separar o cabeçalho dos dados
cabecalho = ['Nome', 'Idade', 'Cidade']
dados_pessoas = [
    ['Ana Silva', 28, 'São Paulo'],
    ['Bruno Costa', 35, 'Rio de Janeiro'],
    ['Carla Dias', 42, 'Belo Horizonte'],
    ['Daniel Faria', 22, 'Curitiba']
]

print("--- Gravador de Dados em CSV ---")

# 3. Solicitar ao usuário o nome do arquivo de saída
nome_arquivo = input("Digite o nome do arquivo CSV a ser criado (ex: contatos.csv): ")

# Uma pequena melhoria: garantir que o nome do arquivo termine com .csv
if not nome_arquivo.lower().endswith('.csv'):
    nome_arquivo += '.csv'

# 4. Usar um bloco try/except para tratar possíveis erros de escrita
try:
    # 5. Abrir o arquivo no modo de escrita ('w' de "write")
    #    'newline=""' é um parâmetro essencial para evitar que o Python crie
    #    linhas em branco entre os seus dados no arquivo final.
    #    'encoding="utf-8"' garante compatibilidade com acentos.
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        
        # 6. Criar o "escritor" de CSV. É ele quem vai formatar e escrever os dados.
        escritor_csv = csv.writer(arquivo_csv)
        
        # 7. Escrever a primeira linha: o cabeçalho (usamos .writerow para uma linha)
        escritor_csv.writerow(cabecalho)
        
        # 8. Escrever todas as outras linhas de dados de uma vez
        #    (usamos .writerows para múltiplas linhas)
        escritor_csv.writerows(dados_pessoas)

    # 9. Se o bloco 'with' terminar sem erros, exibe a mensagem de sucesso
    print(f"\n[SUCESSO] Os dados foram gravados com sucesso no arquivo '{nome_arquivo}'!")

# 10. Capturar erros de I/O (Entrada/Saída), como falta de permissão para criar o arquivo
except IOError as e:
    print(f"\n[ERRO] Não foi possível escrever no arquivo '{nome_arquivo}'.")
    print("Verifique se você tem permissão para criar arquivos nesta pasta.")
    print(f"Detalhe do erro: {e}")