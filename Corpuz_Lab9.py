row = 1
number = 1

User_row = int(input("Please enter the number of rows (positive integer only): "))

if User_row > 0:
    while row <= User_row:
        num_per_row = 1 #first row start

        #The next rows:
        while num_per_row <= row:
            print(f"{number} ", end="")
            number += 1 #number increment
            num_per_row += 1 #number per row
        print(" ") #next line
        row += 1 #row increment
else: 
    print("Enter a positive integer only")
