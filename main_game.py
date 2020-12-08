#Julian Casillas
#Main File

#Import all files you'll need to run this properly
def main():
    
    import main_character as mc
    import wolf
    import section_1
    import section_2
    import section_3
    import section_4


    #Create our player character from our main_character class


    #Intro text to the user
    #The empty input functions are only here so the player has to type something to move on
    #(like pressing a button in a video game to move the dialogue along)
    print("Hello there maze runner!")
    print("Welcome to the maze runner game!")
    input()

    name = input("First, what is your name? ")
    print(name,"is a wonderful name!")
    input()
    print("You have come across the largest maze in the galaxy!")
    input()
    print("Lets hope you are ready for this maze", name)
    
    #And do/say anything else to get your game started



    #Then call your first section.
    #Be sure to pass in your player character
    section_1.start(mc)
    section_2.start(mc)
    section_2.choice(mc)
    section_3.start(mc)
    section_3.oldman(mc)
    section_4.finalbattle(mc)
    section_4.ending(mc)

    repeat = input("Would you like to run again?\nEnter: ")
    if repeat == "Yes":
        main()
    else:
        print("Thank you for playing!", name)
        exit()
    
main()








