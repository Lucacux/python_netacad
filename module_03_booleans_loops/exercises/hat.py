import time
def main ():
    ret_program_welcome = program_welcome()
    ret_user_input_replacement = user_input_replacement(ret_program_welcome)
    eliminate_last_element(ret_program_welcome)
    replace_central_number(ret_program_welcome, ret_user_input_replacement)
    
def program_welcome():
    hat_list = [1,2,3,4,5]
    print("Once upon a time, there was a hat.")
    print("The hat didn't had a bunny, but a list of 5 numbers.")
    print("Those numbers were:", hat_list)
    return hat_list

def user_input_replacement(hat_list):
    print("Please replace the central number of the list (",hat_list[2],")")
    number_replacement = int(input())
    return number_replacement
def eliminate_last_element(hat_list):
    print("Now the hat itself will eliminate the last number of the list.")
    time.sleep(1)
    del hat_list[4]
    return

def replace_central_number(hat_list, number_replacement):
    hat_list = [1,2,number_replacement,4]
    print("You've succesfully replaced the central number of the hat!")
    print("Current hat numbers", hat_list)
    if len(hat_list) < 5:
        print("Wow! The bunny has appeared.")
        print("-Bunny: I hate number five.")
    return

if __name__ == "__main__":
    main()

