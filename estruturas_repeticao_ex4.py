# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
# e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

tx_cresc_a = 0.03
tx_cresc_b = 0.15

pop_a = 80000
pop_b = 20000

n=0

while pop_b <= pop_a:
    pop_a = pop_a*tx_cresc_a + pop_a
    pop_b = pop_b * tx_cresc_b + pop_b

    n+=1

print(f'Após {n + 1} anos a população do país b é {pop_b:.2f} e a dos país a é {pop_a:.2f}')


