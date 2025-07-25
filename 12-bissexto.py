# Pede o ano ao usuário
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Verifica as regras para ser bissexto
# Regra 1: É divisível por 4?
if ano % 4 == 0:
    # Se sim, precisa checar as exceções do século
    # Regra 2: NÃO é divisível por 100?
    if ano % 100 != 0:
        print(f"O ano {ano} É bissexto!")
    # OU é divisível por 400? (Essa é a exceção à exceção do século)
    elif ano % 400 == 0:
        print(f"O ano {ano} É bissexto!")
    else:
        # É divisível por 100 mas não por 400, então não é bissexto (ex: 1900)
        print(f"O ano {ano} NÃO é bissexto.")
else:
    # Não é divisível por 4, então com certeza não é bissexto (ex: 2023)
    print(f"O ano {ano} NÃO é bissexto.")