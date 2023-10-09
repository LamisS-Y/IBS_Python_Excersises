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
for i in range (0, a):
    b=(a-1)-i-1
    print("%"* i+" "+"%"*b)