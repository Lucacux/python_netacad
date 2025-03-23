# Main function
def main():
    ret_test_data = test_data()
    ret_test_results = test_result()
    print_data(ret_test_data, ret_test_results)

# Functions are defined.
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def test_data():
    test_data = [1900, 2000, 2016, 1987]
    return test_data

def test_result():
    test_results = [False, True, True, False]
    return test_results

def print_data(test_data, test_results):
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "->", end=" ")
        result = is_year_leap(yr)
        print(result)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")

if __name__ == "__main__":
    main()
