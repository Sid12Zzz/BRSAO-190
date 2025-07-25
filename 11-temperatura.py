'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''
resultado = 0
temperatura = float(input('Digite uma temperatura: '))
unidade = str(input('Qual é a unidade: [C] [F] [K]').upper())
escolha = str(input('Para qual temperatura você quer converter: [C] [F] [K] ').upper())

if unidade == escolha:
    print('A unidade é a mesma da convertida!')
    exit()


#Celsius para F ou K
if escolha == "C":
    if unidade == 'F':
        resultado = (temperatura - 32) / 1.8
    elif unidade == 'K':
        resultado = temperatura - 273.15


#Farenheirt para C ou K
elif escolha == "F":
    if unidade == 'C':
        resultado = (temperatura * 1.8) + 32
    elif unidade == 'K':
        resultado = ((temperatura - 273.15) * 1.8) + 32 


#Kelvin para C ou F
elif escolha == "K":
    if unidade == 'C':
        resultado = temperatura + 273.15  
    elif unidade == 'F':
        resultado = ((temperatura - 32) / 1.8) + 273.15


print(f"O resultado é: {resultado}")