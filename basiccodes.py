
# function find string greater than length k


def string_k(k, str):

    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:

            string.append(x)
    return string


k = int(input("enter a number: "))
str = input("enter a string: ")
print(string_k(k, str))











radius = int(input("enter the radius of a circle: "))
pi = 3.14
# formulae to find area of circle
area = pi*(radius*radius)

print (f"Area of circle is {area}")

############################## sum of squares of first N natural numbers #######################################################

n = int(input("enter a number: "))
sum=0 

for i in range (n+1):
    i = i**2
    sum = sum+i
    
print(f"sum of squares of {n} natural numbers is {sum}")
    
############################## sum of cubes of first N natural numbers #######################################################

n = int(input("enter a number: "))
sum=0 

for i in range (n+1):
    i = i**3
    sum = sum+i
    
print(f"sum of cubes of first {n} natural numbers is {sum}")
    