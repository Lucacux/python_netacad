# Main function is defined.
def main():
    ret_input_year = input_year()
    ret_leap_year_logic = leap_year_logic(ret_input_year)
# Functions are defined.
def input_year():
    print("Please enter a year to check if it's leap.")
    year = int(input())
    return year
def leap_year_logic(year):

    if year % 4 != 0:
        print(year, "is a common year.")
    elif year % 100 != 0:
        print(year, "is a leap year.")
    elif year % 400 != 0:
        print(year, "is a common year.")
    else:
        leap_year = year
        print(leap_year, "is a leap year.")
    return

if __name__ == "__main__":
    main()