li = [5,2,1,3,4]

n = len(li)

for i in range (n-1):
    for j in range(n-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
print(li)  