
total = totmil = menor = cont = 0
barato = ''
while True:
    product = str(input ('name of the product: '))
    Price = float(input('Price R$'))
    cont += 1
    total += Price
    if Price > 1000:
        totmil += 1
    if cont == 1:
        smaller = Price
        cheap = product
    else:
        if Price < smaller:
            smaller = Price
            cheap = product
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Want to continue? [Y/N]')).strip().upper()[0]
    if answer =='N':
        break
print('end of program. ')
print(f' Total purchase was: {total:2f}')
print(f'We have {totmil} products costing more than R$1000,00')
print(f'The cheapest product was: {cheap}, and it costs R${smaller:.2f}.')