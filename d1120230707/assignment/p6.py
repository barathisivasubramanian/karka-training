def first():
    first=float(input("what is your first number?"))
    second=float(input("what is your second number?"))
    third=float(input("what is your third number?"))
    total=(first+second+third)/2
    return (f"{first}+{second}+{third}/2 is ... {total}")
print(first())

