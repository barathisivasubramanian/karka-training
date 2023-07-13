def old():
    name=(input("Hey, what's your name?"))
    old=int(input(f"ok, {name}, how old are you?"))
    if old<16:
        print("you can't drive")
    if old<18:
        print("you can't vote")    
    if old<25:
        print("you can't rent a car")    
    if old>25:
        print("you can do anything that's legal")
old()            
        
         