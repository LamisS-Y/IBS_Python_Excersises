#Excersise 33 Guess the number
# Write a program that stores a number and the user has to figure it out
# The user can input guesses
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
while True:
    a=8
    b=int(input("Please place your guess: "))
    if b == a:
        print("You found the number 8")
        break
    elif b < a:
        print("The stored number is higher")
    else:
        print("The stored number is lower")
