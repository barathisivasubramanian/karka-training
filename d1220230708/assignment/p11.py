wght=int(input("Please enter your current earth weight:"))
print("I have information for the following plants:\n\t1. Venus\t 2. Mars\t 3. Jupiter\n\t4. Saturn\t 5. Uranus\t 6. Neptune")
plnt=int(input("Which planet are you visiting"))
def weight(a,b):
    if b==1:
        return a*0.78
    if b==2:
        return a*0.39  
    if b==3:
        return a*2.65
    if b==4:
        return a*1.17
    if b==5:
        return a*1.05
    if b==6:
        return a*1.23                  
print(weight(wght,plnt))       



