'''4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.'''

# 1. Importar o módulo datetime para conseguir pegar o ano atual automaticamente.
import datetime

print("--- Calculadora de Idade em Dias ---")

try:
    # 2. Solicitar o ano de nascimento e converter para um número inteiro.
    ano_nascimento = int(input("Por favor, digite o seu ano de nascimento: "))

    # 3. Obter o ano atual usando o datetime.
    # datetime.date.today() pega a data de hoje.
    # .year extrai apenas o ano dessa data.
    ano_atual = datetime.date.today().year

    # 4. Calcular a idade em anos.
    idade_em_anos = ano_atual - ano_nascimento

    # 5. Calcular a idade em dias, desconsiderando anos bissextos (1 ano = 365 dias).
    idade_em_dias = idade_em_anos * 365

    # 6. Exibir o resultado final de forma clara.
    print("\n--- Resultado ---")
    print(f"Ano de Nascimento: {ano_nascimento}")
    print(f"Ano Atual: {ano_atual}")
    print(f"Sua idade aproximada em anos é: {idade_em_anos} anos.")
    print(f"Sua idade aproximada em dias é: {idade_em_dias} dias.")

except ValueError:
    # Bloco para tratar o caso de o usuário não digitar um número válido.
    print("\nErro: Por favor, digite um ano válido com apenas números.")
