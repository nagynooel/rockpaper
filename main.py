from random import randrange
import sys

loop = True
while loop:
    gameloop = False
    menuloop = True
    mainloop = True
    while mainloop:
        print('\n\n\n-----------------------------------------')
        print('----------Rock, paper, scissors----------')
        print('-----------------------------------------')
        print('Welcome player!')
        print('Press enter to start!')
        print('For tutorial type tut to the console!')
        menuloop = True
        while menuloop:
            inp = input()
            if inp == 'exit':
                sys.exit()
            elif inp == 'tut':
                print("\n\n----Tutorial----\nFirst you need to go to the main menu(press enter).\nWhen you are ready to start the game press enter in the main menu.\nType in the number of games you'd like to play.\nThen the game starts. First you need to type in rock, paper or scissors. The robot will choose randomly.\nThe computer will decide who won the round.\nIf you are ready for the next round, than press enter.\nIf you don't want to finish the game than type stop and press enter. This will bring you back to the main menu.\nTo exit the application completely type exit and press enter.\n\nPress enter to go back to the main menu!")
                inp = input()
                if inp == 'exit':
                    sys.exit()
                else:
                    menuloop = False
            elif inp == '':
                startloop = True
                while startloop:
                    print('How many rounds would you like to play?')
                    rounds = input()
                    if not rounds.isdigit():
                        print('Please enter an integer!')
                    else:
                        gameloop = True
                        menuloop = False
                        mainloop = False
                        startloop = False
            else:
                print('Unknown command')

    round = 0

    while gameloop:
        round += 1
        rounds = int(rounds)
        if round > rounds:
            print('Finished')
            gameloop = False
            continue
        if round == 1:
            print('First round:',round,'/',rounds)
        elif round == rounds:
            ex = input()
            if ex == 'exit':
                sys.exit()
            elif ex == 'stop':
                gameloop = False
                validate = False
                iscont = True
                continue
            print('Last round! ',round,'/',rounds)
        else:
            ex = input()
            if ex == 'exit':
                sys.exit()
            elif ex == 'stop':
                gameloop = False
                validate = False
                iscont = True
                continue
            print('Next round:',round,'/',rounds)
        iscont = False
        validate = True
        while validate:
            user = input()
            if user == 'exit':
                sys.exit()
            if user == 'stop':
                gameloop = False
                validate = False
                iscont = True
                continue
            num = randrange(1, 3)
            arr = ['rock', 'paper', 'scissors']
            if user not in arr:
                print('Please give a valid input!')
            else:
                validate = False
        if iscont:
            continue
        print('robot: ', arr[num-1])
        usrnum = arr.index(user) + 1
        if usrnum == num:
            print('Round draw!')
        elif (usrnum == 1 and num == 3) or (usrnum == 2 and num == 1) or (usrnum == 3 and num == 2):
            print('Round won!')
        else:
            print('Round lost!')