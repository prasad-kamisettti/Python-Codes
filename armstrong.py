number = int(input("enter a number: ")) #taking input
original_number = number #Storing the inout number into original number to compare later

sum = 0  #Initilize sum to 0

number_of_digits = len(str(abs(number))) # find the number of digits 

while number > 0: 
    num = number%10 #extract the last digit
    sum = sum+(num**number_of_digits) # number**digits and add it to sum
    number = number//10 # throw the last digit 
    

if sum==original_number:
    print(f"{original_number} is a armstrong number")
else:
    print(f"{original_number} is not an armstrong number")
    