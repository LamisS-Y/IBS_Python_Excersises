#Excersise 32 Draw Diagnal
# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = int(input("Enter the number of rows: "))
print("%"*a)
for i in range(2,a-1):
    b=i-1
    c=(a-3)-(i-1)
    print("%"+b*" "+"%"+c*" "+"%")
print("%"*a)
