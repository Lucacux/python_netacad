def main ():
    menu()
# Functions are defined.
def input_liters_100km():
    print("Please enter how many LITERS PER 100KM do you want to convert to GALLONS PER MILE.")
    l_100km = float(input())

    while l_100km <= 0:
        print("Sorry! The fuel consumption number can only be positive.")
        print("Please enter how many LITERS PER 100KM do you want to convert to GALLONS PER MILE")
        l_100km = float(input())
    return l_100km
      
def input_miles_per_gallon():
    print("Please enter how many MILES PER GALLON do you want to convert to LITERS PER 100KM")
    miles_per_gallon = float(input())

    while miles_per_gallon <= 0:
        print("Sorry! The fuel consumption number can only be positive.")
        print("Please enter how many MILES PER GALLON do you want to convert to LITERS PER 100KM")
        miles_per_gallon = float(input())
    return miles_per_gallon

def liters_100km_to_miles_galon(l_100km):
   
    return 235.215 / l_100km

def miles_per_gallon_to_liters(miles_per_gallon):
    return 235.215 / miles_per_gallon

def print_total_liters_to_miles(l_100km, miles_per_gallon):
    print("The equivalent of (",l_100km,") LITERS PER KM in MILES PER GALLON is:", miles_per_gallon,"MPG")
    return

def print_total_miles_per_gallon_to_liters(miles_per_gallon, l_100km):
    print("The equivalent of (",miles_per_gallon,") MILES PER GALLON in LITERS PER KILOMETER is:",l_100km,"L/100KM")
    return
def menu():
    print("Please select an option:")
    print("1. Convert LITERS PER KILOMETER to MILES PER GALLON")
    print("2. Convert MILES PER GALLON to LITERS PER KILOMETER.")
    option = int(input())
    if (option == 1):
        ret_input_liters = input_liters_100km()
        ret_liters_100km_to_miles_gallon = liters_100km_to_miles_galon(ret_input_liters)
        print_total_liters_to_miles(ret_input_liters, ret_liters_100km_to_miles_gallon)
    elif (option == 2):
        ret_input_miles_per_gallon = input_miles_per_gallon()
        ret_miles_per_gallon_to_liters = miles_per_gallon_to_liters(ret_input_miles_per_gallon)
        print_total_miles_per_gallon_to_liters(ret_input_miles_per_gallon, ret_miles_per_gallon_to_liters)
    return
if __name__ == "__main__":
    main()





    


