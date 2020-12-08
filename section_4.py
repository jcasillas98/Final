#importing rqeuired files
import main_character as mc
import wolf

#start of the section
def finalbattle(player):
    print("Great job on defeating the old man! The finish line is so close!!")
    input()
    print("Oh no...")
    input()
    print("The wolf has caught up!")
    input()
    print("Quick! There are three paths to take!")
    input()
    print("Choose a path and lets hope you are able to trick the wolf!")
    

    choice = input("What will you choose?!\n\"L\" - Move Left\n\"R\" - Move right\n\"F\" - Move Forward\nEnter: ")
    while choice not in ('L','R','F'):
        choice = input("Please input\n\"L\" - To move Left\n\"R\" - To move right Right\n\"F\" - To move Forward\nEnter: ")
    #User makes a choice that affects the amount of lifes left
    if choice == 'L':
        print("Oh no! The wolf picked that side too! He has attacked you!")
        user = wolf.villian("Wolf", 1)
        user.attack()
        user.over()
        input()

    if choice == 'R':
        print("Good choice! You have a clear path!")
        input()

    if choice == 'F':
        print("Good choice! You have a clear path!")
        input()
#Ending of the game 
def ending(player):
    print("You have made it to the finish line!")
    input()
    print("Congratulations! You have defeated the maze and the big bad wolf!")
    input()
    print("GAME OVER!")
    
    

    
          
