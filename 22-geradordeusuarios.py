'''2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.'''

import requests
try:
    api_random = "https://randomuser.me/api/"

    # 1. GUARDE _a resposta completa da API em uma variável.
    resposta = requests.get("https://randomuser.me/api/")

    dados = resposta.json()
    usuario = dados['results'][0]


    #nome completo
    primeiro_nome = usuario['name']['first']
    ultimo_nome = usuario['name']['last']
    nome_completo = primeiro_nome +' ' + ultimo_nome

    #email
    email = usuario['email']

    #pais
    pais = usuario['location']['country']

    #elular
    celular = usuario['phone']


    print(f'Nome do usuario: {nome_completo}\nPais: {pais}\nEmail: {email}\nCelular: {celular}\n')

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
