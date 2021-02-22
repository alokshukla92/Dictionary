import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w == 'end/':
        return "exit"
    elif w in data.keys():
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Do You mean %s ?. Press Y if yes , press N if No : " % get_close_matches(w, data.keys())[0])
        if yn.upper() == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        if yn.upper() == 'N':
            return "We cant find your input ! Try again "
    else:
        return "Item Not found ! Try again with correct item"

while True:
    word = input("\n Note: Press end/ to exit the program \n Enter the word : ")
    output = translate(word)
    if type(output) == list:
        for i in output:
            print("\n Here's the defination : ")
            print(i)

    elif output == 'exit':
        break
    else:
        print(output)


