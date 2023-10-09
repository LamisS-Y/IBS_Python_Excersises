#Exercise 17 Average of Input
# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

number_1= int(input("enter 1st number: "))
number_2= int(input("enter 2ed number: "))    
number_3= int(input("enter 3rd number: "))
number_4= int(input("enter 4th nubmer: "))
number_5= int(input("enter 5th number: "))
sum= number_1+number_2+number_3+number_4+number_5
average= sum/5
print("your numbers sum and average: ")
print("sum: ",sum," average: ",average)
