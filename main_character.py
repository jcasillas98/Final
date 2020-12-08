    #define your variables here

    #example:
    #money = 0
    #attack = 4
class User:
    def __init__(self, bag, lives):
        self.bag = bag
        self.lives = lives
    def displayBag(self):
        print(self.bag)

    def inventory(self):
        inventory = []
        if self.bag == "Shield":
            inventory.append("Shield")
            print(inventory)
        else:
            inventory.append("Empty")
            print(inventory)
    
    
    

    
    

    
    #define any functions here
def choice():
    print("Should I move left or right?")
    choice == "left"
    print("You have turned left")
    choice == "Right"
    print("You have turned right")
    
    


    #Pay attention to your indents!
    
