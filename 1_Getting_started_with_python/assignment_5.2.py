#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except
#and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
#Invalid input
#Maximum is 10
#Minimum is 2
    #elif num != int or float : break
    #print("Enter number, not a word!")

large = None
small = None

while True:
    n = input("Enter an integer number (or 'done' to exit): ")

    if n == 'done':
        break

    try:
        num = int(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if large is None or num > large:
        large = num

    if small is None or num < small:
        small = num

if large and small is not None:
    print("Maximum is", large)
    print("Minimum is", small)
else:
    print("Neither maximum nor minimum")
