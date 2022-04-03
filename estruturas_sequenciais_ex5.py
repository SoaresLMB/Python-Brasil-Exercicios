# Faça um Programa que converta metros para centímetros.

parar = False

while not parar:
     valor_metro = float(input("Insira o valor em metros que deseja converter para cm:"))
     conversao = valor_metro * 100

     print(conversao, "cm")

     escolha = int(input("digite (1) para encerrar e (2) para nova conversão:"))

     if escolha == 1:
        parar = True
        print("Conversor encerrado!")
     else:
        parar = False




