#Exercise 11 Variable Mutation
# a = 3
# make the "a" variable's value bigger by 10
# print(a)

# b = 100
# make b smaller by 7
# print(b)

# c = 44
# please double c's value
# print(c) 

# d = 125
# please divide by 5 d's value
# print(d)

# e = 8
# please cube of e's value
# print(e)

# f1 = 123
# f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)

# g1 = 350
# g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)

# h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)

# i1 = 10
# i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)

# j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)
a=3
a += 10
print(a)
b=100
b -= 7
print(b)
c=44
c *= 2
print(c)
d=125
d /=5
print(d)
e=8
e **= 3
print(e)
g1=350
g2=200
print((g2*2)>g1)
h=1357988018575474
h=1357988018575474
if h % 11 ==0:
    print("h is devided by 11")
else:
    print("h cannoct be devided by11")
i1=10
i2=3
i2_squared= i2**2
i2_cubed=i2**3
print(i1>i2_squared and i1<i2_cubed)
j=1521
print((j % 3==0) or (j % 5==0))