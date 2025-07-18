############### program to interchange the first and last element of a list #################################################

my_list = [1,2,3,4]
my_list[0],my_list[-1] = my_list[-1],my_list[0]
print(f"updated list after swapping first and last element is {my_list}")

################################### using functions and temp variable #############################################################
def swapList(my_list):
    size = len(my_list)
    
    temp = my_list[0]
    my_list[0] = my_list[size-1]
    my_list[size-1] = temp
    return my_list
my_list = list(map(int, input("Enter a numbers seperated by space: ").split()))

print(swapList(my_list))

#################################### program to find multiply all numbers in list #############################################################

my_list = list(map(int, input("Enter a numbers seperated by space: ").split()))
multi = 1
for val in my_list:
    multi = multi*val
print(multi)