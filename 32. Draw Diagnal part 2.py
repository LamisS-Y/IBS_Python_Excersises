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
for i in range(a):
    if i == 0 or i ==a - 1:
        print("%" * a)
    else:
       line = "%" + " " * (((a - 2))//2) + "%"+" " * (((a - 2))//2) + "%"
       print(line)
