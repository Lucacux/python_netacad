def main():
    ret_beatles_list = beatles_list()
    add_beatles_members(ret_beatles_list)
    ret_beatles_list = user_input_beatles_members(ret_beatles_list)
    erase_beatles_members(ret_beatles_list)
    add_ringo_to_beatles(ret_beatles_list)
    print_all_current_members(ret_beatles_list)

def beatles_list():
    beatles = []
    return beatles

def add_beatles_members(beatles):
    beatles.extend(["John Lennon", "Paul McCartney", "George Harrison"])
    print("Current The Beatles members:", beatles)
    return

def user_input_beatles_members(beatles):
    print("Please add 'Stu Sutcliffe' and 'Pete Best' to the band")
    for i in range(2):
        new_beatles = input()
        beatles.append(new_beatles)
    return beatles

def erase_beatles_members(beatles):
    print("Stu Sutcliffe and Pete Best will be removed from the band.")
    print("After that, Ringo Starr will be added to the band.")
    try:
        beatles.remove("Stu Sutcliffe")
        beatles.remove("Pete Best")
    except ValueError:
        print("One or both members were not found in the list.")
    return

def add_ringo_to_beatles(beatles):

    print("Stu Sutcliffe and Pete Best were succesfully removed from the band.")
    beatles.insert(0, "Ringo Starr")
    print("Adding Ringo Starr ...")
    return

def print_all_current_members(beatles):
    print("Ringo was added successfully!")
    print(beatles, "Are the current beatles of the band.")
    return
if __name__ == "__main__":
    main()
