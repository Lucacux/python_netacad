# Main function is defined.
def main ():
    ret_year = input_year()
    ret_months = input_months()
    is_leap_year(ret_year)
    ret_months_days = months_days(ret_year, ret_months)
    print_data(ret_year,ret_months,ret_months_days)
# Functions are defined.
def input_year():
    print("Welcome to (year/month) calculator to (days).")
    print("Please enter the amount of years that you want to calculate")
    # Equal to do-while validation.
    years = int(input())
    while years <= 0:
        print("Please enter a positive amount of years.")
        years = int(input())
    return years

def input_months():
    print("Now enter the amount of months that you want to calculate.")
    months = int(input())
    # Equal to do-while validation.
    while months > 12 or months < 1:
        print("Please enter a valid month (1-12)")
        months = int(input())
    return months

def is_leap_year(years):
    if years % 4 != 0:
        return False
    elif years % 100 != 0:
        return True
    elif years % 400 != 0:
        return False
    else:
        return True
    
def months_days(years, months):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if months == 2 and is_leap_year(years):
        return 29
    
    return month_days[months - 1]
def print_data(years,months,month_days):
    print("The month", months, "of year", years, "has", month_days,"days.")
    return
if __name__ == "__main__":
    main()
