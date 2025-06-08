import random
def game():
    choices=['snake','water','gun']
    while True:
        computer = random.choice(choices)
        player = input("enter your choice: [Snake,Water,Gun] or quit to exit: ").lower()
        print("Compuer chose:",computer)
        print("You chose:",player)
        if player == 'quit':
            print("Thanks for playing!")
            break
        if player not in choices:
            print("Invalid Choice")
        else:
            if player == computer:
                print("its a draw!")
            elif (player == 'snake' and computer=='water') or\
                (player== 'water' and computer=='gun')or\
                (player=='gun' and computer == 'snake'):
                print("You win!")
            else:
                print("Computer wins!")
game()            

