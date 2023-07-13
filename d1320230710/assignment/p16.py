gender=input("What is your gender (Male or Female):\n")
first_name=input("First name:\n")
last_name=input("Last name:\n")
age=int(input("Age:\n"))
married=input("Are you married, Karthick (yes or no)?\n")
def older():
    if gender=="Female":
        if age>20:
            if married=="yes":
                print("Then I shall call you Mrs.Barathi")  
    if gender=="Male":
        if age>21:
            print("Then I shall call you Mr.Karthick")      
older()       
    