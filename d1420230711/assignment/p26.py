print("Ye Olde Keychain Shoppe")
def choice():
    print("1. Add Keychains to Order\n2. Remove Keychains from Order\n3. View Current Order\n4. Checkout")
    key=int(input("Please enter your choice:"))
    if key==1:
        print("ADD KEYCHAINS")
        choice()
    if key==2:
        print("REMOVE KEYCHAINS") 
        choice() 
    if key==3:
        print("VIEW CURRENT ORDER")
        choice()
    if key==4:
        print("CHECKOUT")  
choice()        


