'''4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. 
O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  
'''
import requests
try:
    moeda = input('Qual o codigo da moeda: ').upper()
    url_api = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    requisicao = requests.get(url_api)
    resposta = requisicao.jason()
    resposta = resposta.status_code
    if resposta.status_code == 404:
        print(f"\n[ERRO] O código de moeda '{moeda}' é inválido ou não foi encontrado.")
        
    parametro = moeda + 'BRL'
    val_max = resposta[parametro]['high']
    val_min = resposta[parametro]['low']
    data_att = resposta[parametro]['create_date']
    bid = resposta[parametro]['bid']
    print('Abaixo estão a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.')
    print(val_max)
    print(val_min)
    print(data_att)
    print(bid)


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
#print(val_max)