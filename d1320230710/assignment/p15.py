print("TWO MORE QUESTIONS, BABY!\n Think of something and I'll try to guess it!")
both=" "
alive=input("Q1) Does it stay inside or outside or both?\n")
lve=input("Q2) Is it a living thing\n") 
def vle():
    if alive=="outside" and lve=="yes": 
        both="bison"
    if alive=="outside" and lve=="no":
        both="billboard"  
    if alive=="inside" and lve=="yes":  
        both="houseplant"  
    if alive=="inside" and lve=="no":
        both="shower curtain"    
    if alive=="both" and lve=="yes":
        both="dog" 
    if alive=="both" and lve=="no":
        both="cell phone"   
    print(f"Then what else could you be thinking of besides a python {both}!")
vle()  

