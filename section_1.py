#import anything you need here
import main_character as mc
import random
         
#This function is called by main_game.
#This will control the whole section
#It'll need the player character as an input in order to interact with them
def start(player):
    print("Your task is to complete the maze!")
    input()
    print("You will ony have one life, so make decisions wisely!")
    print("Firstly...")
    input()
    choice = input("At what time would you like to explore the maze?\n\"N\" - At night\n\"D\" - During the day\nEnter: ").upper()
    while choice not in ('N', 'D'):
        choice = input("Please input\n\"N\" - At night\n\"D\" - During the day\nEnter: ")
    if choice == 'N':
        print("You are a brave one!")
        input()
        print("You are rewarded for your bravery, a shield was added to your bag")
        user = mc.User("Shield", 1)
        user.inventory()
        print("You now walk into the maze!")
    if choice == "D":
        print("You are a clever one! A sheild was added to your bag")
        user = mc.User("Shield",1)
        user.inventory()
        print("You now walk into the maze!")
    
    
    
    
          
            
     
  
 

    #Be sure to ask the player for input to decide what to do as you go
