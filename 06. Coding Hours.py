#Excersise 6 Coding Hours
# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52
avg_coding_hr = 6
semester_weeks = 17
work_days = 5
print(work_days*semester_weeks*avg_coding_hr)
avg_work_hr_weekly = 52
Total_coding_hr = avg_coding_hr*semester_weeks*work_days
total_work_hr = avg_work_hr_weekly*semester_weeks
perc_coding_hr = (Total_coding_hr/total_work_hr)*100
print(perc_coding_hr, "%")