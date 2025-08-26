li = list(map(int, input("Enter numbers separated by space: ").split())) #user inputs


n = len(li)

for i in range (n-1):
    for j in range(n-1-i): # inner loop for comparison
        if li[j]>li[j+1]: 
            li[j],li[j+1] = li[j+1],li[j] #Swapping
print(li)  