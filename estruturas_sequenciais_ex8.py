# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print("**********************")
print("***Cálculo Salarial***")
print("**********************")

salario_hora = float(input("Digite o salário/hora:"))
horas_diaria = float(input("Digite a carga horaria diária:"))
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados no mês:"))

salario_mes = salario_hora * horas_diaria * dias_trabalhados

possui_extra = input("Foi realizado hora extra? Responda com (sim) ou (não)").upper()

if possui_extra == "SIM":
    qtd_hora_extra =float(input("Digite o total de horas extras trabalhadas:"))

    hora_extra = salario_hora + salario_hora * 0.5
    total_hora_extra = qtd_hora_extra * hora_extra
    salario_mes_mais_extra = salario_mes + total_hora_extra

    print("Salario do mês {} reais".format(salario_mes_mais_extra))
else:
    print("Salário do mês: {} reais.".format(salario_mes))






