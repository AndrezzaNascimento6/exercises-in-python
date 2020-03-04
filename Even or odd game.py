from random import randint
v= 0
while True:
    player = int(input('Say a value: '))
    computer = randint(0,10)
    total = player + computer
    type = ' '
    while type not in 'EO':
        type = str(input('Even or odd? [E/O]')).strip().upper()[0]
    print(f'You played {player} and the computer {computer}. Total of {total} ', end='')
    print("IT'S EVEN" if total % 2 == 0 else " It's ODD ")
    if type == 'E':
        if total % 2 == 0:
            print('YOU WIN')
            v += 1
        else:
            print('YOU LOSE...')
            break
    elif type == 'O':
        if total %2 == 1:
            print('YOU WIN')
            v +=1
        else:
            print('YOU LOSE.!')
            break
        print("Let's play again ! ! !")
    print(f'GAME OVER! You won {v} times.')
