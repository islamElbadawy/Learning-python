import json
from difflib import get_close_matches

with open("dicData.json") as data_file:
    data = json.load(open("dicData.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0 :
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("y for yes or n for no : ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("You have pressed wrong keys. ")
        else:
            return("You have entered wrong input just y or n")
    
    else:
        return("You entered wrong word")


word = input("Enter the word you want to search : ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
