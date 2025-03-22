# Main function.
def main():
    ret_input_number = input_number()
    evaluate_condition(ret_input_number)
# Functions are defined.
def input_number():
    print("Please enter a number to check if it is higher than 100.")
    number = int(input())
    return number
def evaluate_condition(number):
    if(number > 100):
        print(number,"is higher than 100.")
    else:
        print(number,"is lower than 100.")
    return

if __name__ == "__main__":
    main()