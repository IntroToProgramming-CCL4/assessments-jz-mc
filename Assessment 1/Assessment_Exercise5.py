months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} 
month_number = int(input("Enter a month number between (1-12), from January to December: ")) #To make the value an integer to make it easier to handle
if month_number > 0:
    print("Please choose a number from 1-12")
if 1 <= month_number <= 12:
    if month_number == 2: #To check if its leap year or not
        leap_year = input("Is it leap year? (yes/no): ").lower()
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        elif leap_year == "no":
            print("February has 28 days in a non-leap year.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    else:
         # For all other months
        print(f"The month {month_number} has {months[month_number]} days.")
else:
    print("Command cannot be executed. Please enter a number between 1 and 12.")