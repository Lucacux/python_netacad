print("Metric system to Imperial calculator.")
print("Please select an option")
print("1. KM to Miles\n 2. Miles to KM")

option = int(input())

if option == 1:
 print("Please enter how many KM do you want to convert to MILES")
 km = float(input())
 miles = km * 0.621371
 print(km, "KM equals to", miles,"MILES")

elif option == 2:
 print("Please enter how many MILES do you want to convert")
 miles = float(input())
 km = miles * 1.61
 print(miles,"MILES equals to", km,"KM")

else:
 print("Invalid option, please select either 1 or 2.")

