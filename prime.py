import math

# input from the user
number = int(input("Enter a number: "))

#check if number is less than or equal to 1
if number <= 1:
    print(f"{number} is not a prime number")
else:
    prime = True
    for i in range(2, int(math.sqrt(number)) + 1):     #Loop from 2 to sqrt(num)
        if number % i == 0:
            prime = False
            break
    
    if prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
