# 1. Importar o módulo necessário
import csv

# 2. Inicializar a variável acumuladora ANTES de tudo
total_vendas = 0

print("--- Processador de Vendas CSV ---")

# 3. Bloco 'try' para lidar com o arquivo
try:
    # 4. Abrir o arquivo de forma segura
    with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
        
        # 5. Criar o leitor de CSV
        leitor_csv = csv.reader(arquivo)
        
        # 6. Pular o cabeçalho
        next(leitor_csv)
        
        # 7. Iniciar o laço para processar cada linha de dados
        for linha in leitor_csv:
            try:
                # 8. Converter os textos para os tipos numéricos corretos
                quantidade = int(linha[1])
                preco_unitario = float(linha[2])
                
                # 9. Calcular o subtotal da linha
                subtotal = quantidade * preco_unitario
                
                # 10. Acumular o subtotal no total geral
                total_vendas += subtotal

            # Trata o erro caso alguma linha tenha dados inválidos
            except (ValueError, IndexError):
                print(f"[Aviso] Linha com formato inválido ignorada: {linha}")

    # 11. Após o fim do laço, imprimir o resultado final formatado
    print("\n--- Relatório Final ---")
    print(f"O valor total das vendas é: R$ {total_vendas:.2f}")

# 12. Capturar o erro se o arquivo não for encontrado
except FileNotFoundError:
    print("\n[ERRO] O arquivo 'produtos.csv' não foi encontrado.")
    print("Por favor, crie o arquivo na mesma pasta que o programa.")