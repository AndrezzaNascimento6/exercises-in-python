from random import randint
computer = randint (0,10)

print("I'm your computer, I just thought of a number between 0 and 10.")
print("Can you imagine what was?")
gotit = False #porque você ainda não acertou.
guesses = 0
while not gotit: #enquanto o acertou de cima ainda n funcionou.
    gamer = int(input("Qual o seu palpite? "))
    palpites += 1 #palpite recebe, palpite mais um.
    if gamer == computer:
        gotit = True
    else:
        if gamer < computer:
            print("Try a larger number...")
        elif gamer > computer:
            print('Try a smaller number...')
print('got it right with {} attempts. CONGRATULATIONS'.format((guesses))