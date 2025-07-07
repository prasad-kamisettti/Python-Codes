# even_numbers = []

# for number in range (1,100):
#     if number%2==0:
#         even_numbers.append(str(number))
        
# print("The numbers are:"," ".join(even_numbers))

even_numbers = []
prime_numbers = []

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(str(number))
    if is_prime(number):
        prime_numbers.append(str(number))

print("The even numbers are:", " ".join(even_numbers))
print("The prime numbers are:", " ".join(prime_numbers))
