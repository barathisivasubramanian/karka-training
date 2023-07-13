y=int(input("enter the year:"))
def check_eligiblity(y):
    if y>2021 and y<=2023:
        return("he is eligible")
    else:
        return("he is not eligible")
if_eligible=check_eligiblity(y)
print(if_eligible)