# Main function is defined
def main():
    x_value = get_input()
    y_value = calculate_y(x_value)
    print_values(x_value,y_value)
# Trying to do exercise with functions
def get_input():
    print("Please enter a value for x")
    x = float(input())
    return x
def calculate_y(x):
    y = 1./(x + 1./(x + 1./(x + 1./x)))
    return y
def print_values(x,y):
    print("Previous value of x:",x,"\nCurrent value (y):", y)
if __name__ == "__main__":
    main()