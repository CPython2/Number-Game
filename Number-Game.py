import random
name=input("What is your name?")
game=input("Hello " + name + "! would you like to play a game? press g to play my game")
if game=="g":
    print("This is a guessing game. I am thinking of a number between 1 and 50. You have five chances to answer correctly.")
    firnum=input("What is your first guess?")
    firnum=float(input())
    if firnum < ran:
        print("My number is higher.")
    if firnum > ran:
        print("My number is lower.")
    if firnum == ran:
        print('Well Done, " + name ". You have guessed my number!')
    secnum=input("What is your second guess?")
    secnum=float(input())
    if secnum < ran:
        print("My number is higher.")
    if secnum > ran:
        print("My number is lower.")
    if secnum == ran:
        print("Well Done, " + name + ". You have guessed my number!")
    trinum=input("What is your third guess?")
    trinum=float(input())
    if trinum < ran:
        print("My number is higher.")
    if trinum > ran:
        print("My number is lower.")
    if trinum == ran:
        print("Well Done, " + name + ". You have guessed my number!")
    fornum=input("What is your fourth guess?")
    fornum=float(input())
    if fornum < ran:
        print("My number is higher.")
    if fornum > ran:
        print("My number is lower.")
    if fornum == ran:
        print("Well Done, " + name + ". You have guessed my number!")
    fifnum=input("What is your fifh guess?")
    fifnum=float(input())
    if fifnum < ran:
        print("My number is higher.")
    if fifnum > ran:
        print("My number is lower.")
    if fifnum == ran:
        print("Well Done, " + name + ". You have guessed my number!")
    else:
        print("Sorry " + name + ", my number was", ran)
    
