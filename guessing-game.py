guess = "whale"
print("Hello! Are you ready to play a guessing game?")
print("Try guessing the animal. This animal lives in the water and is one of the biggest in the ocean!")
awnser1 = input("ready?").lower()
while awnser1 == "yes" :
    awnser2 = input("What is your guess?").lower()
    if awnser2[0] == "q":
       awnser1 = "No"
    elif awnser2 == guess :
        print("Well done! You're a genius! Thank you for playing!")
        awnser1 = "no"
    else:
        print("Good guess but that is not right. Another hint is that they eat barnacle")