'''3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro.
 Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.'''
import requests
cep = input('Digite o Cep: ')


try:
    url_API = f"https://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(url_API).json()

    # logradouro
    logradouro = requisicao['logradouro']

    # bairro
    bairro = requisicao['bairro']
    #  cidade
    cidade = requisicao['localidade']
    #  estado
    estado = requisicao['estado']
    # e o próprio CEP.
    puxar_cep = requisicao['cep']
    print(puxar_cep, estado, cidade, bairro,)

    
except requests.exceptions.HTTPError as e:
    print(f"Erro na Resposta da API: O servidor retornou um erro.")
    print(f"Código de status: {e.response.status_code}") 

except requests.exceptions.Timeout as e:
    print("Erro de Tempo Limite (Timeout): O servidor demorou muito para responder.")

except requests.exceptions.JSONDecodeError:
    print("Erro de Decodificação: A resposta não é um JSON válido.")

except (KeyError, IndexError):
    print("Erro de Estrutura: O formato dos dados mudou e não encontrei as informações.")

except TypeError:
    print('Seus dados não estão em formato json!')

