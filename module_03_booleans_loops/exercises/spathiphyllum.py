# Main function is defined
def main():
    ret_input_spati = input_spati()
    spati_evaluation(ret_input_spati)
# Functions are defined.
def input_spati():
    print("Please enter any word\nHint: Type Spathi or SPATHI")
    spathi = input()
    return spathi
def spati_evaluation(spathi):
    if spathi == "SPATHI":
        print("Yes, the Spathiphyllum is the best plant of all times!")
    elif spathi == "spathi":
        print("No, I want a bigger Spathiphyllum!")
        print("Hint: Type 'SPATHI'")
    else:
        print("Maybe you should buy a Spathiphyllum...")
        print("Spathiphyllum!, not:",spathi)
        print("Hint: Type spathi or SPATHI")

        return
if __name__ == "__main__":
    main()
