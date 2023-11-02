import random
uscore= cscore = 0
choices = ['rock', 'paper', 'scissor']
flag = True

while flag == True:
    user_choice = input('Your turn(R/P/S/1): ')
    pc_choice = random.choice(choices)

    if user_choice == 'R':
        if pc_choice == 'rock':
            print("match tie")

        elif pc_choice == 'scissor':
            uscore += 1
            print('user +1')

        elif pc_choice == 'paper':
            uscore += 1
            print('user +1')


    elif user_choice == 'S':
        if pc_choice == 'rock':
            cscore +=1
            print('computer +1')

        elif pc_choice == 'scissor':
            print("match tie")

        elif pc_choice == 'paper':
            uscore += 1
            print('user +1')


    elif user_choice == 'P':
        if pc_choice == 'rock':
            cscore +=1
            print('computer +1')

        elif pc_choice == 'scissor':
            cscore +=1
            print('computer +1')

        elif pc_choice == 'paper':
            print("match tie")

    elif user_choice == '1':
        flag = False
        print("User scores:{} \nComputer Scores:{}".format(uscore,cscore))
    else:
        print('error')


