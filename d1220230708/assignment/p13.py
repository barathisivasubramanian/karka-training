def objct():
    ans=" "
    print("Two questions!\nThink of an object, and I'll try to guess it.")
    ab=(input("Question 1) Is it animal,vegetable or mineral?\n"))
    cd=(input("Question 2) Is it bigger than a breadbox\n"))
    if ab=="animal":
        if cd=="yes":
            ans="moose"
        elif cd=="no":
            ans="sqiurrel"  
    if ab=="vegetable":
        if cd=="yes":
            ans="watermelon"    
        elif cd=="no":
            ans="carrot"
    if ab=="mineral":
        if cd=="yes":
            ans="paper clip"
        elif cd=="no":
            ans="camaro"                    
    print(f"My guess is that you are thinking of a {ans}\nI would ask you if I'm right, but I don't actually care.")
objct()    


