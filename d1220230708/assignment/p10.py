def age():
    name=input("Hey, what's your name? (sorry, I keep forgetting)")
    age=int(input(f"ok,{name} how old are you?"))
    if age<16:
        print(f"You can't drive {name}")
    if age>=16 and age<=17:
        print(f"You can drive but not vote {name}")    
    if age>=18 and age<=24:
        print(f"You can vote but not rent a car {name}")
    if age>25:
        print(f"You can do pretty much anything {name}")   
age()   
