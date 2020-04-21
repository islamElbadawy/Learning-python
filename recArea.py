print("Program to calculate rectangle area and parameter")
width = float(input("Enter the width of rectangle: "))
height = float(input("Enter the height of rectangle: "))

while True:
    process = input("What do you want to calculat area or parameter\n write \"a\" for area : \n write \"p\" for parameter : \n and \"q\" to close : \n ")
    if process == "a" :
        print("The area of rectangel = ", height*width, "\n")
    elif process == "p" :
        print("The parameter of rectangel = ", (height+width)*2, "\n")
    elif process == "q" :
        break
    else : 
        print("Unknown process \n")