# ############### program to interchange the first and last element of a list #################################################

# my_list = [1,2,3,4]
# my_list[0],my_list[-1] = my_list[-1],my_list[0]
# print(f"updated list after swapping first and last element is {my_list}")

# ################################### using functions and temp variable #############################################################
# def swapList(my_list):
#     size = len(my_list)
    
#     temp = my_list[0]
#     my_list[0] = my_list[size-1]
#     my_list[size-1] = temp
#     return my_list
# my_list = list(map(int, input("Enter a numbers seperated by space: ").split()))

# print(swapList(my_list))

# #################################### program to find multiply all numbers in list #############################################################

# my_list = list(map(int, input("Enter a numbers seperated by space: ").split()))
# multi = 1
# for val in my_list:
#     multi = multi*val
# print(multi)


# #################################### program to find multiply all numbers in list using built-in functions #############################################################
# import math
# my_list = list(map(int, input("Enter a numbers seperated by space: ").split()))
# result = math.prod(my_list)
# print(result)

# #################################### program to find sum of all numbers in list  #############################################################
# # my_list = list(map(int, input("Enter a numbers seperated by space: ").split()))
# # multi = 0
# # for val in my_list:
# #     multi = multi+val   ## or you can directly find by using built in function in python called "sum"
# # print(multi)


# #################################### program to print all even numbers in a range  #############################################################

n = int(input("Enter a number to find all the even numbers: "))

for i in range(n+1):
    if i%2==0:
        print(i)