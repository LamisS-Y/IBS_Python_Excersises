#Excersise 34 Parametric Average
# Write a program that asks for a number
# It would ask this many times to enter an integer
# If all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
print("Find the numbers that will achive the following:")
print("Sum: 22 and Average: 4.4")
while True:
    try:
        amount=int(input("How many number do you want to enter? "))
        if 2<= amount <= 6: #added the parameter to stop the loop from being too long
            break
        else:
            print("the number chosen is not acceptable")
    except: ValueError
    print("Invalid input, Please enter a number between 2 and 6")
Numbers = []
for i in range(amount):
    b=int(input("Please enter one number at a time: "))
    Numbers.append(b)
print("you have entered the following numbers")
for num in Numbers:
    print(num)
sum= sum(Numbers)
print("your numbers sum is: ",sum)
avg= sum/amount
print("your numbers average is: ",avg)
if sum==22 and avg==4.4:
    print("You have found the correct numbers")
else:
    print("Your numbers are incorrect they do not match what we are looking for")