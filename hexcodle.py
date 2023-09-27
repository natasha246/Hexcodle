import random

# generate a hexcode
# get user input for guess
# check the user's input and tell them if each digit is correct or not (and how to change it)


# generate hex code for user to guess
hexlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

target = ""
# create loop  to add to the hexcode string
for i in range(6):
    pos = random.randint(0,14)
    target+=hexlist[pos]

# get user input---------------------------------------------
counter = 0


# store the return message for the guess
while counter < 6:
    # make sure all digits are valid
    valid = True   
    if counter == 5:
        print("You ran out of guesses! The answer was " + target)
        break
    result = ""
    guess = input("Enter your guess: ")
    # make it upper case
    guess = guess.upper()
    if guess == target:
        print("OOOOOO\nCorrect!")
        break
    if len(guess)!=6:
        print("Guess must be 6 digits long. Try again.")
        continue
    for i in range(6):
        currentG = guess[i]
        currentT = target[i]

        # check if all the digits in the guess are valid
        for i in range (6):
            if currentG not in hexlist:
                valid = False
                print("Your guess contained an invalid digit. Try again.")
                break

        # if the digit is correct
        if currentG==currentT:
            result+="O"
        elif currentG>currentT:
            result+="v"
        else: 
            result+="^"
    if valid == True:
        counter +=1
    print("guess: " + str(counter))
    print(result)
    print("target:" + target)
    print("guess:" + guess)
    print("-------------------------")




