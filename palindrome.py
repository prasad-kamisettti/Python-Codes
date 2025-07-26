# a = input("enter a input: ")
# rev = (a[::-1])
# if (rev==a):
#     print(f"the given input {a} is a palindrome")  
# else:
#     print(f"the given input {a} is not palindrome")


##### two pointer approach 

a = input("enter a input to check palindrome: ")
left = 0
right = (len(a)-1)
while left < right:
    if (a[left]!=a[right]):
        print(f"{a} is not a palindrome")    
        break
    else:
        left =left+1
        right = right-1
    break
print("palindrome")
        
# Get input from the user
string = input("Enter a string: ")

# Reverse the string manually
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string  

# Compare original and reversed
if string == reversed_string:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
