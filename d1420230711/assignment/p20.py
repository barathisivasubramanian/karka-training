print("I will add up the numbers you give me.")
sum=int(input("Enter the number"))
total_num=0
for i in range(100):
    if sum==total_num:
        print("break")
    elif sum==total_num+1:
        print(f"The total so far is {total_num}")  
 
