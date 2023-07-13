def quiz():
    score=0
    qz=(input("Are you ready for a quiz?"))
    print("Okay, here it comes!")
    sk=int(input("Q1) What is the capital of Alaska?\n\t 1) Melbourne \n\t 2) Anchorage \n\t 3) Juneau\n"))
    if sk==3:
        print("It's correct")
        score=score+1
    else:
        print("It's wrong")   
    zy=int(input("Q2) Can you store the value 'cat' in a variable of type int?\n\t 1) Yes\n\t 2) No\n"))
    if zy==2:  
        print("It's yes") 
        score=score+1
    else:
        print("Its wrong")
    ab=int(input("Q3) What is the result of 9+6/3?\n\t 1)5\n\t 2)11\n"))
    if ab==2:
        print("It's yes")
        score=score+1
    else:
        print("Its wrong") 
        score=score+1
    print(f"overall, you got {score} out of 3 correct.\n Thanks for playing!")      
quiz()
  


        




