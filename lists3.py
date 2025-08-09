# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,


# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

#
expense = ["January 2200", "feb 2350", "march 2600", "april 2130", "may 2190"]
print(expense)

#1
print(int(expense[1].split()[1]) - int(expense[0].split()[1]))

#2
print(int(expense[0].split()[1]) + int(expense[1].split()[1]) + int(expense[3].split()[1])) 

#3
print(2000 in [int(item.split()[1]) for item in expense])

#4
expense.insert(5, "June: 1980") 
print(expense)


#5
expense = ["January 2200", "feb 2350", "march 2600", "april 2130", "may 2190"]

for i in range (len(expense)):
    if expense[i].startswith("april"):
        amt = int(expense[i].split()[1]) - 200
        expense[i]= f"april {amt}"
print(expense)






