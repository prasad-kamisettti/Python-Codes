############### program to interchange the first and last element of a list #################################################

my_list = [1,2,3,4]
my_list[0],my_list[-1] = my_list[-1],my_list[0]
print(f"updated list after swapping first and last element is {my_list}")
