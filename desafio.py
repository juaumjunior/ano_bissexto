ano = int(input("informe o ano dosejado: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano informado se trata de um ano bissexto pois ele possui 366 dias!")
else:
    print("O ano informado não se tata de um ano bissexto pois ele possui 365 dias!")