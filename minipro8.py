# Author - Kishan Sindhi
# date - 30-5-2021
# discription - this function take the year as input from the user
# and in return it tells that the entered tear us a leap yaer or not

year = int(input("Enter a year you want to check that is a leap year or not:\n"))
if year % 4 == 0:
    print("Year is leap year")
else:
    print("Year is not a leap year")
