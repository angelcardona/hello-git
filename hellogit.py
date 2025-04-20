def product():
    x=int(input("Please introduce a number: "))
    y=int(input("Please introduce a number: "))
    if y != 0:
        c=x/y
        
        print(f"The result of division is {c}")
    else :
        return print("Division by cero doesn't exist")
    
    
product()
