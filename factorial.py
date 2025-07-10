n= int(input("enter a number: "))
fact = 1
for i in range(1, n+1):
    fact = fact*n
    n=n-1
print(fact)
    