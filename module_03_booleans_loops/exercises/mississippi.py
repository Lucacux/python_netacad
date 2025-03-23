# Module time for sleep function is defined
import time 
# Main functon is defined.
def main ():
    for_cylce()
    
def for_cylce():
    mississipi_counter = 5

    for i in range (mississipi_counter):
        print(i,"Mississipi")
        time.sleep(1)
    print("Ready or not, here I come!")

if __name__ == "__main__":
    main()