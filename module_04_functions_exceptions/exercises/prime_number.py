# Main function is defined
def main():
    ret_number = input_number()
    is_prime(ret_number)
# Functions are defined.
def input_number():
    print("Please enter a number to check if it's a prime number.")
    number = int(input())
    while number <= 0:
        print("Please enter a positive number.")
        number = int(input())
    return number
def is_prime(number):
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not prime.")
            return False
    print(number, "is prime.")
    return True
if __name__ == "__main__":
    main()
