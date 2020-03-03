price = float(input('total amount payable : R$'))

print('Payment methods\n'
    '[ 1 ] In cash \n'
    '[ 2 ] Card \n'
    '[ 3 ] 2x on the card \n'
    '[ 4 ] 3x on the card')


opt = int(input('Enter payment method: '))


if opt == 1:
    final = price- (price * 0.10)
    print('Purchase of R $ {:. 2f} will cost R $ {:. 2f} at the end'.format(price, final))
    print('Discount of R${:.2f}'.format(price- final))
elif opt == 2:
    final = price - (price* 0.05)
    print('Purchase of R $ {:. 2f} will cost R $ {:. 2f} at the end'.format(price, final))
    print('Discount of '.format(price - final))
elif opt == 3:
    print('There is no discount. Final value R${:.2f}'.format(price))
elif opt == 4:
    tranche = int(input('How many installments?'))
    final = price+ (price * 0.20)
    print('Your purchase in installments at {} x R $ {: 2f} with INTEREST of R${}'.format(tranche, (final / tranche), (final - price)))
    print('Purchase of R $ {:. 2f} will cost R $ {:. 2f} at the end'.format(price, final))
else:
    print('Option chosen invalid')


