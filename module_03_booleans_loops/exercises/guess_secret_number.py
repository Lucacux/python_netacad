# Main function is defined
def main():
    number_to_guess_value = number_to_guess()
    guess_logic(number_to_guess_value)

# Functions are defined.
def input_number():
    print("Please enter a number between 1 and 100:")
    user_guess = int(input())
    return user_guess

def number_to_guess():
    return 50

def guess_logic(number_to_guess):
    user_guess = 0
    while user_guess != number_to_guess:
        user_guess = input_number()
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number (",number_to_guess,")")
            return

if __name__ == "__main__":
    main()
