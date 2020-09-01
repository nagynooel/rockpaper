from random import randrange

run = True

while run:
    user = input()
    num = randrange(1, 3)
    arr = ['rock','paper','scissors']
    if user not in arr:
        print('Please give a valid input!')
        continue
    print('robot: ',arr[num-1])
    usrnum = arr.index(user) + 1
    if usrnum == num:
        print('Draw')
    elif (usrnum == 1 and num == 3) or (usrnum == 2 and num == 1) or (usrnum == 3 and num == 2):
        print('You won!')
    else:
        print('You lost')