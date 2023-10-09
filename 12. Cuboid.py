#Excercise 12 Cuboid
# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
length, width, height = 10.0, 10.0, 10.0
surface_area=2*(length*width)+2*(length*height)+2*(height*width)
volume=length*width*height
print("Surface Area:", surface_area)
print("volume:",volume)