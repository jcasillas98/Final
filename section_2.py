#importing rqeuired files
import main_character as mc
import wolf


#start of the section
def start(player):
    print("A huge obsticle that you will face while completing this maze is the big bad wolf")
    input()
    print("Every wrong move you make will cause you to face the wolf!")
    input()
#User makes a choice that affects the amount of lifes 
def choice(player):
    choice = input("You have a choice to make!\n\"L\" - Move Left\n\"R\" - Move right\nEnter: ")
    while choice not in ('L','R'):
        choice = input("Please input\n\"L\" - To move Left\n\"R\" - To move right\nEnter: ")
    if choice == 'L':
        print("You are in the clear! lets keep moving!")
        input()

    if choice == 'R':
        print("Oh no! You are now cornered! The wolf has attacked you! You have now lost your life!!")
        user = wolf.villian("Wolf", 1)
        user.attack()
        user.over()
        
    
        
   


     

    

