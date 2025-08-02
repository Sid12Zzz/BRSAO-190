# 1. Importar o módulo json, que já vem com o Python
import json

# 2. Criar um dicionário Python com os dados da pessoa
dados_pessoa = {
    "nome": "Mariana Santos",
    "idade": 34,
    "cidade": "Curitiba",
    "profissão": "Engenheira de Software",
    "hobbies": ["leitura", "corrida", "fotografia"]
}

print("--- Gravador e Leitor de Arquivo JSON ---")

# 3. Solicitar ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo a ser criado (ex: dados.json): ")

# Melhoria: garantir que o nome do arquivo termine com .json
if not nome_arquivo.lower().endswith('.json'):
    nome_arquivo += '.json'


# --- PARTE 1: Escrevendo no Arquivo JSON ---

print(f"\nTentando salvar os dados no arquivo '{nome_arquivo}'...")
try:
    # 4. Abrir o arquivo no modo de escrita ('w')
    #    'encoding="utf-8"' garante que acentos e símbolos sejam salvos corretamente
    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json:
        
        # 5. Usar json.dump() para escrever o dicionário no arquivo
        #    'indent=4' é um argumento opcional que deixa o arquivo formatado e legível
        json.dump(dados_pessoa, arquivo_json, indent=4, ensure_ascii=False)

    print(f"[SUCESSO] Os dados foram gravados com sucesso!")

# 6. Tratar possíveis erros de permissão de escrita
except IOError as e:
    print(f"[ERRO] Não foi possível escrever no arquivo '{nome_arquivo}'.")
    print(f"Detalhe do erro: {e}")
    # Se não conseguimos escrever, não adianta tentar ler. Encerramos o programa.
    exit()


# --- PARTE 2: Lendo o Arquivo JSON ---

print(f"\nLendo os dados de volta do arquivo '{nome_arquivo}'...")
try:
    # 7. Abrir o mesmo arquivo, agora no modo de leitura ('r')
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_json:
        
        # 8. Usar json.load() para carregar os dados do arquivo de volta para uma variável Python
        dados_carregados = json.load(arquivo_json)

    # 9. Imprimir os dados carregados para confirmar que funcionou
    print("[SUCESSO] Dados carregados do arquivo:")
    print("---------------------------------")
    # Imprimindo de uma forma bonita
    for chave, valor in dados_carregados.items():
        print(f"{chave.capitalize()}: {valor}")
    print("---------------------------------")

# 10. Tratar o erro caso o arquivo não seja encontrado
except FileNotFoundError:
    print(f"[ERRO] O arquivo '{nome_arquivo}' não foi encontrado para leitura.")
# Tratar o erro caso o arquivo esteja corrompido ou não seja um JSON válido
except json.JSONDecodeError:
    print(f"[ERRO] O arquivo '{nome_arquivo}' não é um arquivo JSON válido.")