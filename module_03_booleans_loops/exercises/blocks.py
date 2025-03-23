# Main functions is defined.
def main():
    ret_blocks_input = blocks_input()
    ret_pyramid_logic = pyramid_logic(ret_blocks_input)
    pyiramid_height(ret_pyramid_logic)
# Functions are defined.   
def blocks_input():
    print("Please enter the number of blocks")
    blocks = int(input())
    return blocks
def pyramid_logic(blocks):
    height = 0
    layers = 1
    while blocks >= layers:
        blocks -= layers
        height += 1
        layers += 1
    return height


def pyiramid_height(height):
    print("The pyramid height equals to:", height)
    return
if __name__ == "__main__":
    main()