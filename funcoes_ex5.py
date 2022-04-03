#Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
# e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def imposto (taxa_imposto, custo):
    taxa_convertida = taxa_imposto/100
    custo_adicional = custo*taxa_convertida
    custo_total = custo + custo_adicional
    return custo_total

#VERIFICAÇÃO:

imp_1 = imposto(50,400)
print(f"Valor a pagar: {imp_1}")



