#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
# de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

parar = False

tx_cresc_a = 0.03
tx_cresc_b = 0.15

nova_pop_a = [80000]
nova_pop_b = [20000]

n = 0

while not parar:
    pop_a = nova_pop_a[n]*tx_cresc_a + nova_pop_a[n]
    nova_pop_a.append(pop_a)

    pop_b = nova_pop_b[n]*tx_cresc_b + nova_pop_b[n]
    nova_pop_b.append(pop_b)

    if nova_pop_b [n] >= nova_pop_a [n]:
        print(f'Após {n +1} anos a população do país b é {nova_pop_b [n]:.2f} e a dos país a é {nova_pop_a [n]:.2f}')
        parar = True

    else:
        parar = False

    n+=1

