import random
name = input("Enter your name: ")


def hangman():
    word = random.choice(["pugger", "naruto", "sasuki", "jiraya", "itachi", "hashirama", "madara"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessMade = ""
    while len(word) > 0:
        main = ""
        for letter in word :
            if letter in guessMade:
                main += letter
            else :
                main += "_"
        
        if main == word:
            print(main)
            print("You won!")
            break
        
        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessMade += guess
        else:
            print("Please enter a valid character.")
        
        if guess not in word:
            turns -= 1 
            if turns == 9 :
                print(" 9 turns left!")
                print("---------")
            elif turns == 8:
                print(" 8 turns left!")
                print("---------")
                print("    0    ")
            elif turns == 7 :
                print(" 7 turns left!")
                print("---------")
                print("    0    ")
                print("    |    ")
            elif turns == 6 :
                print(" 6 turns left!")
                print("---------")
                print("    0    ")
                print("    |    ")
                print("   /     ")
            elif turns == 5 :
                print(" 5 turns left!")
                print("---------")
                print("    0    ")
                print("    |    ")
                print("   / \    ")
            elif turns == 4 :
                print(" 4 turns left!")
                print("---------")
                print("  \ 0    ")
                print("    |    ")
                print("   / \    ")
            elif turns == 3 :
                print(" 3 turns left!")
                print("---------")
                print("  \ 0 /  ")
                print("    |    ")
                print("   / \    ")
            elif turns == 2:
                print(" 2 turns left!")
                print("---------")
                print("  \ 0 /| ")
                print("    |    ")
                print("   / \    ")
            elif turns == 1:
                print(" 1 turn left!")
                print("---------")
                print("  \ 0_|/ ")
                print("    |    ")
                print("   / \    ")
            elif turns == 0:
                print(" You lost!")
                print("You let a kind man die!")
                print("---------")
                print("    0_|  ")
                print("   /|\   ")
                print("   / \    ")
                break


print("Welcome", name)
print("---------------")
print("Try to guess the word in less than 10 attempts. ")

hangman()

