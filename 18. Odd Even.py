#Exercise  18 Odd Even
# Write a program that reads a number from the standard input,
# then prints "Odd" if the number is odd, or "Even" if it is even.
number = int(input("Enter the number: "))
if number % 2 == 0: 
    print("the number you entered is even")
else:
    print("the number you entered is odd")
