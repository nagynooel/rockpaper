from random import randrange

gameloop = False
menuloop = True

print('-----------------------------------------')
print('----------Rock, paper, scissors----------')
print('-----------------------------------------')
print('Welcome player!')
print('Press enter to start!')
print('For tutorial type tut to the console!')
while menuloop:
    inp = input()
    if inp == 'tut':
        print('Tutorial will be available soon!')
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
        print('First round:')
    else:
        print('Next round:')
    user = input()
    num = randrange(1, 3)
    arr = ['rock', 'paper', 'scissors']
    if user not in arr:
        print('Please give a valid input!')
        continue
    print('robot: ', arr[num-1])
    usrnum = arr.index(user) + 1
    if usrnum == num:
        print('Draw')
    elif (usrnum == 1 and num == 3) or (usrnum == 2 and num == 1) or (usrnum == 3 and num == 2):
        print('You won!')
    else:
        print('You lost')