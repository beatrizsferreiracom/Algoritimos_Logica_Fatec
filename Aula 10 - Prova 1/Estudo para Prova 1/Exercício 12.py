#12) Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das categorias:

idade = int(input('Insira a idade do nadador: '))

if idade >= 5 and idade <= 7:
    print('Infantil A')
elif idade >= 8 and idade <= 10:
    print('Infantil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Adulto')
else:
    print('Idade inválida')