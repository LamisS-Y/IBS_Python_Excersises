#Excersice 30 Draw Diamond
# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
a = int(input("Please enter number of rows: "))
if a % 2 == 0:
    for b in range (1, a+1, 2):
        c= (a - b) // 2
        print(" "*c + "*"* b) 
    for d in range (a-1, 0, -2):
        e= (a - d) // 2
        print(" "*e + "*"* d) 
else:
    for f in range (1, a+1, 2):
        c= (a -f) // 2
        print(" "*c + "*"* f) 
    for g in range (a-2, -1, -2):
        e= (a -g) // 2
        print(" "*e + "*"* g) 
