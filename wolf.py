import main_character as mc
from os import sys

#class name 
class villian:
    
    #A function that takes perameters
    def __init__(self, name, lives):
        self.lives = lives
        self.name = name
    def attack(self):
        self.lives -= 1
        print(self.lives)
    def over(self):
        if self.lives == 0:
            print("Thank you for playing!")
            print("GAME OVER")
            sys.exit(0)
  
           
            
        
        
        
        
        
    
        
    
    
    
    #takes the totallives varibale set in main character file and subtracts one
       
    


    
