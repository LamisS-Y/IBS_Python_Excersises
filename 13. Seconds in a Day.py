#Exercise 13 Seconds in a Day
# current_hours = 14;
# current_minutes = 34;
# current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables above

current_hours=14
current_minutes=34
current_seconds=42
print((24*3600)-((current_hours*3600)+(current_minutes*60)+current_seconds))