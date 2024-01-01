#4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of time-and-a-half in a function called computepay()
#and use the function to do the computation.
#The function should return a value.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input unless you want to -
#you can assume the user types numbers properly.
#Do not name your variable sum or use the sum() function.

hour=float(input("Enter hours:"))
rate=float(input("Enter rate:"))
def computepay(hour,rate):
    if hour<40:
        pay=rate*hour
    else:
        pay=(hour-40)*(rate*10.50) + (40 * rate)
    return pay

p=computepay(hour,rate)
print(p)