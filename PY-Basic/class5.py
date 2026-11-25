# Loops
# Loops are used for repeating a block of code until or while a condition is met

# while loop
i = 0
while i < 20:
    print(i)
    i += 2

even_num = 0 

# incrementing in 2 
while even_num < 20:
    print(even_num)
    even_num += 2

# Looping through a list or a tupple using while loop

items = ["omo", "broom", "dettol"]
item = 0
while (item <len(items)):
    print(items[item])
    item += 1

#

fruits = ["pawpaw","apple", "pineapple", "orange"]
fru = 0

while (fru <len(fruits)):
    print(f"{fruits[fru]}'s")
    fru += 1

# find the sum    number in the list 
nums = [2, 4, 6, 8 ,10]
sum = 0
n = 0

while n< len(nums):
    sum += nums[n]
    print(sum)
    n += 1

# Count from 0 to 15 add add it togethe

count = 0
total = 0
while count <= 15:
    total = total + count
    print(total)
    count += 1

# for Loop 

letters = ['ark', 'Beth', 'Bathel']

for i in letters:
    print(i)


# Go through the tuple and use the for loop to print everything 
my_nums = (1,2,3,4,5,6)

for numbers in my_nums:
    print(numbers)


# counting from 0 to 9

for numbers in range (0, 9, 1):
    print(numbers)