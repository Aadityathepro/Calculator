import random
l = ['rock', 'paper', 'scissor']
while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game start...........
    1 Yes
    2 No | Exit 
    '''))
    if uc > 2:
        print('Invalid input. Starting again...')
        continue
    if uc == 1:
        for a in range(1, 4):
            user_input = int(input('''
            1 Rock
            2 Paper
            3 Scissor
            '''))
            if user_input > 3:
                print('Invalid input. Starting again...')
                break
            if user_input == 1:
                uchoice = 'rock'  # User choice
            elif user_input == 2:
                uchoice = 'paper'
            elif user_input == 3:
                uchoice = 'scissor'
            cchoice = random.choice(l)  # Computer choice
            print('Computer value:', cchoice)
            print('User value:', uchoice)
            if cchoice == uchoice:
                print('Game Draw')
                ucount += 1
                ccount += 1
            elif (uchoice == 'rock' and cchoice == 'scissor') or \
                    (uchoice == 'paper' and cchoice == 'rock') or \
                    (uchoice == 'scissor' and cchoice == 'paper'):
                print('You win')
                ucount += 1
            else:
                print('Computer wins')
                ccount += 1
            print(" ")
        if ucount == ccount:
            print('Game Draw...')
        elif ucount > ccount:
            print('You win the game...')
        else:
            print('Computer wins the game...')
        print('User Score:', ucount)
        print('Computer Score:', ccount)
    else:
        break
