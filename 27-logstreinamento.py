# 1. Importar a biblioteca pandas (o 'pd' é um apelido padrão da comunidade)
import pandas as pd

print("--- Analisador de Logs de Treinamento ---")

# 2. Solicitar ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo CSV de logs (ex: logs_treinamento.csv): ")

try:
    # 3. Ler os dados usando pandas. Ele cria uma "tabela" (DataFrame) na memória.
    #    O 'pd.read_csv' já lida com a abertura, leitura e fechamento do arquivo.
    print(f"Lendo o arquivo '{nome_arquivo}'...")
    df = pd.read_csv(nome_arquivo)

    # 4. Acessar a coluna desejada pelo nome
    #    'df['tempo_execucao']' seleciona a coluna inteira como uma série de dados.
    coluna_tempo = df['tempo_execucao']

    # 5. Calcular a média e o desvio padrão com os métodos do pandas
    media = coluna_tempo.mean()
    desvio_padrao = coluna_tempo.std()

    # 6. Exibir os resultados formatados com duas casas decimais
    print("\n--- Resultados da Análise ---")
    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")

# 7. TRATAMENTO DE ERROS

# Trata o erro se o arquivo não for encontrado
except FileNotFoundError:
    print(f"\n[ERRO] O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Verifique se o nome foi digitado corretamente e se ele está na mesma pasta.")

# Trata o erro se a coluna 'tempo_execucao' não existir no arquivo
except KeyError:
    print(f"\n[ERRO] O arquivo '{nome_arquivo}' não contém a coluna 'tempo_execucao'.")
    print("Por favor, verifique o cabeçalho do seu arquivo CSV.")

# Trata outros erros, como dados não numéricos na coluna de tempo
except Exception as e:
    print(f"\n[ERRO] Ocorreu um problema ao processar o arquivo.")
    print(f"Verifique se a coluna 'tempo_execucao' contém apenas números.")
    print(f"Detalhe do erro: {e}")