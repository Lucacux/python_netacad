# Main functions is defined
def main ():
    ret_program_list = program_list()
    ret_new_list = new_list(ret_program_list)
    ret_sort_new_list = sort_new_list(ret_new_list)
    print_list(ret_sort_new_list)
# Functions are defined.
def program_list():
    program_list = [1,2,4,4,1,4,2,6,2,9]
    return program_list
def new_list(program_list):
    new_list = list(set(program_list))
    return new_list
def sort_new_list(new_list_sorted):
    new_list_sorted.sort()
    return new_list_sorted
def print_list(new_list_sorted):
    print("The list, now sorted and managed properly is:", new_list_sorted)    
    return
if __name__ == "__main__":
    main()