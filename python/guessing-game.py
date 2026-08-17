import random

def playgame():
    luck = random.randint(1,50)

    while(True):
        guess = int(input("Enter the lucky number:"))

        if(guess==luck):
            print("YOU won!")
        elif(guess>luck):
            print("Too high!")
        elif(guess<luck):
            print("Too low!")
        else:
            print("Invalid number")

playgame()