#7) O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos 
#(aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, 
#escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custoF = float(input('Digite o custo de fábrica do carro: R$'))

impostos = 0.28 + 0.45
custoC = custoF + (custoF * impostos)

print('O custo ao consumidor é de R$' + str(round(custoC,2)))