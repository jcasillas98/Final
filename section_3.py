#importing rqeuired files
import main_character as mc
import wolf
import random

#start of the section
def start(player):
    print("Great job on makeing the correct decision! You are doing very well! Keep it going!")
    input()
    print("Quick! You have another choice to make!")
    choice = input("What will you choose this time?!\n\"L\" - Move Left\n\"R\" - Move right\nEnter: ")
    while choice not in ('L','R'):
        choice = input("Please input\n\"L\" - To move Left\n\"R\" - To move right\nEnter: ")
    #User makes a choice that affects the amount of lifes left
    if choice == 'L':
        print("Oh no! You are now cornered! The wolf has attacked you! You have now lost your life")
        user = wolf.villian("Wolf", 1)
        user.attack()
        user.over()
        input()

    if choice == 'R':
        print("Good choice! You have a clear path!")
        input()
#User confronts roadblock and based on random chnaces, the lifes will be affected
def oldman(player):
    print("Looks like you have come across an old man.")
    input()
    print("Oh no! the old man wants to challange you to a dice rolling game!")
    input()
    print("You will both roll a dice, whoever has the highest number wins! If you lose you lose your life.")

    run = True
    while run:
        user_input = input("Press enter to roll dice!")
        print()

        roll = random.randint(1,6) 
        roll2 = random.randint(1,6)

        if roll > roll2:
            print("You have won")
            input()
            print("You rolled a", roll,"and old man rolled a ",roll2)
            run = False
        elif roll < roll2:
            print ("You have lost, you rolled a ", roll,"and old man rolled a ",roll2)
            run = False
            user = wolf.villian("Wolf", 1)
            user.attack()
            user.over()
        elif roll == roll2:
            print("It is a tie, you rolled a ", roll,"and old man rolled a ",roll2)
            print("Lets go again")
        else:
            run = False
    
    
          
        
       
