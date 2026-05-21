import os
os.system('cls')

def is_leap_year(godina):
    if( godina % 4 ==0 and ((godina % 100 != 0) or (godina % 400 == 0))):
        print(f"Year {godina} is a leap year.")
    else:
        print(f"Year {godina} is not a leap year.")

year = int(input("Which year do you want to check? "))
is_leap_year(year)