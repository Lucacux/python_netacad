# Main function is defined
def main():
 ret_enter_PIT = enter_PIT()
 ret_PI_18_percentage = PI_18_percentage(ret_enter_PIT)
 ret_PI_32_percentage = PI_32_percentage(ret_PI_18_percentage)
 ret_calculate_PIT_tax = calculate_PIT_tax(ret_enter_PIT, ret_PI_18_percentage, ret_PI_32_percentage)
 print_data(ret_calculate_PIT_tax)
# PIT stands for Personal Income tax
def enter_PIT():
    print("Please enter your personal income")
    personal_income = float(input())
    return personal_income

def PI_18_percentage(personal_income):
    PIT_percentage_18 = personal_income * 0.18
    return PIT_percentage_18

def PI_32_percentage(personal_income):
    PIT_percentage_32 = personal_income * 0.32
    return PIT_percentage_32

def calculate_PIT_tax(personal_income, PIT_percentage_18, PIT_percentage_32):
    if personal_income <= 0:
        PIT_tax = 0
    elif personal_income < 85.528: # 85.258 is the equivalent amount from the hypotetic currency.
        PIT_tax = PIT_percentage_18 - 556.02 # Tax exemption (556.02)
    elif personal_income > 82.528:
        PIT_tax = 14.839 + 0.2 * PIT_percentage_32
        return PIT_tax
    
def print_data(PIT_Tax):
    print("The tax value is: (", PIT_Tax, ") dollars.")
    return

if __name__ == "__main__":
    main()

