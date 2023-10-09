#Excersise 35 Draw Chess Table
# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
a=int(input("please enter number of line: "))
for i in range (a):
    b=a-i
    if i % 2 == 0:
        print("%"*i+"%"*b)
    else:
        print(" "*2+"%"*i+"%"*b)
