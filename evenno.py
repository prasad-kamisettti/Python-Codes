even_numbers = []

for number in range (1,100):
    if number%2==0:
        even_numbers.append(str(number))
        
print("The numbers are:"," ".join(even_numbers))