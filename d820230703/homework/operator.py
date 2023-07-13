first=int(input("enter the first number"))
operator=(input("enter the operator"))
second=int(input("enter the third number"))
def operator_result(first,operator,second):
    if operator=="+":
        return(first+second)
    if operator=="-":
        return(first-second)
    if operator=="*":
        return(first*second)   
    if operator=="**":
        return(first**second)
    if operator=="/":
        return(first/second)    
    if operator=="//":
        return(first//second)
   print(operator_result(first,operator,second))
        
