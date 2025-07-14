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

#####  second way #########

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1): # range should be 2 to n//2+1
        if n % i == 0: 
            return False
    return True

num = int(input("Enter a number: ")) #take input from the user

if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
