while True : 
    print("Options: ")
    print("Type \"add\" to add two numbers")
    print("Type \"sub\" to subtract two numbers")
    print("Type \"multiply\" to multibly two numbers")
    print("Type \"divide\" to devide two numbers")
    print("Type \"quit\" to close program")
    operator = input(": ")
    if operator == "add" :
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the seconde number: "))
        print (num1 + num2)
        break
    elif operator == "sub" :
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the seconde number: "))
        print( num1 - num2)
        break
    elif operator == "multiply" :
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the seconde number: "))
        print( num1 * num2)
        break
    elif operator == "divide" :
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the seconde number: "))
        print( num1 / num2)
        break
    elif operator == "quit" :
        break  
    else :
        print("Unknown input")  