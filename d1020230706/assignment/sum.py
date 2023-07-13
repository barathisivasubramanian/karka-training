marks=[96,72,80,67,82]
total_marks=0
print(marks)

enum_marks=enumerate(marks)  
print(type(enum_marks))
for i,mark in enum_marks:
    print("entering iteration process for item:"+str(i))
    print("before sum",total_marks)
    total_marks=total_marks+mark
    print("after sum",total_marks)
    print("existing iteration process for item:"+str(i))
    print("\n")


# print("sum",sum)
# avg=sum/len(x)
# print("average of the x:",avg)

# x=[500,200,300,400]
# z=[]
# for i in x:
#     b="INR"+str(i)
#     z.append(b)
# print(z)

# x=["apple","fav","food"]
# for i, num(x)
# b=len>4
# print(x)










    
