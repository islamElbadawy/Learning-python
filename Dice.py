import random 

print("This is a Dice simulator. ")

x = "y"

while x == "y" : 
    number = random.randint(1,6)
    if number == 1 :
        print("==========")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("===========")
    elif number == 2 :
        print("==========")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("===========")
    elif number == 3 :
        print("==========")
        print("|0        |")
        print("|    0    |")
        print("|       0 |")
        print("===========")
    elif number == 4 :
        print("==========")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("===========")
    elif number == 5 :
        print("==========")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("===========")
    elif number == 6 :
        print("==========")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("===========")
    x = input("y to roll it again or anything else to quit : ")
