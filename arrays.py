##################################### Code to find sum of an array #################################################################

array = list(map(int,input("enter numbers seperated by space: ").split()))
sum=0
for i in array:
    sum = sum+i  
print(sum)


################################### code to find maximum of an array without using built in function ###############################

array = list(map(int,input("enter numbers seperated by space: ").split()))
maximum = array[0]
n= len(array)
for i in range (n):
    if array[i]>maximum:
        maximum = array[i]
print(maximum)

##################################### code to find maximum of an array using built in function ######################################

array = list(map(int,input("enter numbers seperated by space: ").split()))
print(max(array))


##################################### code to perform array rotation ######################################

array = list(map(int,input("enter numbers seperated by space: ").split()))
r = int(input("enter a number to perform shift "))
rotated_array = array[r:]+array[:r]
print(f"Array after rotation is {rotated_array}")



##################################### code to perform left or right array rotation as per user requirements ######################################

array = list(map(int,input("Enter numbers seperated by space: ").split()))
r = int(input("Enter a number to perform shift: "))
which_shift = input("Type which shift you want Left or Right? ").lower()

if(which_shift=="left"):
    rotated_array = array[r:]+array[:r]
    print(f"Array after left rotation by {r} shift is {rotated_array}")
elif(which_shift=="right"):
    rotated_array = array[-r:]+array[:-r]
    print(f"Array after right rotation by {r} shift is {rotated_array}")
else:
    print("Invalid Input")


##################################### Program for Find remainder of array multiplication divided by n ######################################

array = list(map(int,input("Enter numbers seperated by space: ").split()))
n = int(input("enter a number: "))
product = 1
for i in array:
           product = product*i
result = product%n
print(f"The remainder of array multiplication divided by {n} is {result}")