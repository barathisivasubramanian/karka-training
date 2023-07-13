print("WELCOME TO METOHELL'S TINY ADVENTURE!")
room1=(input("You are is a creepy house! would you like to go 'apstairs' or into the 'kitchen'?\n"))
def room():
    if room1=="kitchen":
        place=input("There is a long countertap with dirty dishes everywhere, off to one side there is, as you'd expect, a refrigeator, You may open the 'refrigerator' or losk in a 'cabinet'.\n")
        if place=="refrigerator":
                room2=input("Inside the refrigerator you see food and stuff, It losks pretty masty, Would you like to eat some of the food? ('yes' or 'no')\n")
                if room2=="yes":
                    print("You don't die of starvation...eventually")
                else:
                    print("You die of starvation...eventually")
                    if room1=="apstairs":
                        print("You die of starvation...eventually")                     
room()                        
                