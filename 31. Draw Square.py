#Excersice 31 Draw Square
# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was
a = int(input("Please enter number of rows: "))
print("%"*a)
for i in range (1,a-1):
    i="%"
    space= a-2
    print(i+" "*space+i)
print("%"*a)
#different method
# a = int(input("Enter the number of rows: "))
# for i in range(a):
    # if i == 0 or i ==a - 1:
        # print("%" * a)
    # else:
       # line = "%" + " " * (a - 2) + "%"
        # print(line)
