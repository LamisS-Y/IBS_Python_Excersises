#Exsercise 21 Party Indicator
# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second represents the number of boys
#
# If the the number of girls and boys are equal and 20 or more people are coming to the party
# it should print: The party is excellent!
#
# If there are 20 or more people coming to the party but the girl - boy ratio is not 1-1
# it should print: Quite a cool party!
#
# If there are less people coming than 20
# it should print: Average party...
#
# If no girls are coming, regardless the count of the people
# it should print: Sausage party
girls= int(input("enter number of girls: "))
boys= int(input("enter number of boys: "))
total=girls+boys
if total >= 20:
    if girls == boys:
        print("The party is excellent!")
    else:
        print("Quite a cool party")
elif total < 20 and girls > 0: 
    print("Average party")
else:
    print("Sausage party")
