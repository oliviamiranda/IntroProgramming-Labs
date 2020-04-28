colornames = ["RED", "BLUE", "YELLOW","GREEN"]
def title():
    print("Color Preference Evaluator")
def promptForColor():
    color = input("what color do you want to enter?")
    return color.strip().upper()
def confirmColor(x):
    y = input("you entered "+ x + " is that correct? (y/n)")
    if y.strip().lower() == 'y':
        return True
    else:
        return False

def containsElement(x):
    global colornames
    for i in colornames:
        if i == x:
            return True
    return False

def praiseUser():
    print("nice job!")
def ridiculeUser():
    print("you're bad at this")
def main():
    title()
    col = promptForColor()
    confirmColor(col)
    confirm = containsElement(col)
    if confirm == True:
        praiseUser()
    else:
        ridiculeUser()

main()
    