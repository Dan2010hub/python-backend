# Advanced data types

#List
fruits = list (["mango", "pawpaw", "apple"]) # list(): is used to convert other data type to a list 

fruits.append("Cashew") # Append is used to add somethign to a list
fruits.remove("apple") # .remove is use to remove items from the list
print(fruits)

# Tuple

nums = (2,4,6,8,4)
# tuple cant be updated which makes it the difference between a list and a tuple
print(nums)

# Sets 
# Sets doesn't have an index

arrange = set([1, 3, 5, 2, 9])
print(arrange)

# Dicitionaries 
person_data = {
    "name": " Chimdindu Daniel",
    "age": 16,
    "is_male": True
}

print(person_data["age"])

# built-in-Methods 

#Len() returns the total number of items in the tuple, list 
print(len(fruits))

#max () returns the largest element 
print(max(nums))

#min() Returns the smallest element
print(min(nums))

#Sum adds all numerical items together 
print(sum(nums))

# sorted() Returns a new sorted list containing the tuple's element
print(sorted(nums))


subjects = list(["Maths","Physics", "Chemistry", "English"])
print(subjects)

country = ("Nigeria", "Canada", "Italy")
print(country)

personal_bio = {
    "name": " Daniel Chimdindu",
    "age": 16,
    "Favourite_p-lang": "Python"
}

sett =set([1,2,3,4,5,5,5,9,8])
print(sett)

# Adding elements 
# Append is a single item x to the very end of the list

fruits.append("banana")
print(fruits)

# extend, Appends every individual item from another list or iterable to the end of the current list
fruits.extend(["cowpea", "Melon"])
print(fruits)

# Removing elements 
fruits.remove("cowpea")
print(fruits)

# pop
fruits.pop(0)
print(fruits)

# Searching and Counting 

print(fruits.index('pawpaw'))

fruits.append("pawpaw")

print(fruits.count("pawpaw"))

# Reodering and copying
# sort
# Is used to arrange from A to Z
fruits.sort()
print(fruits)

# Reverse 
# Is to turn the list upside down
fruits.reverse()
print(fruits)

# Copy
# returns a shallow copy of a list
new_list = fruits.copy()
new_list.append("orange")
print("original:", fruits)
print("copy:", new_list)


# Tuple methods

# Tuple has only 2 methods 
# 1. count
# the count () returns the number of times a specified value apperas in a tuple
print(nums.count(8))

# 2. index
# the index methods returns the index of the first occurance of a specificed vale in the tuple, if the value is not found it raises a valueeError

print(nums.index(4))

# SET ()

#. Add 
arrange.add(8)
print(arrange)

#.Update add many items at once 

arrange.update([7,6,4])
print(arrange)

# remove
arrange.remove(3)
print(arrange)

# Discard, Remove item if item is not present it will keep quiet no error
arrange.discard(4)
print(arrange)

# pop, remove any one item you can't choose each which one

arrange.pop()
print(arrange)

# Clear remove anything 

#arrange.clear()
print(arrange)

# Copy, use to make photocopy
numbers = arrange.copy
print(numbers)
print(arrange)

# maths in set

set1 = {'mango', 'pawpaw','banana'}
set2 = {'banana', 'orange', 'cashew'}

# Union Join them together no duplicate

# print(set1.union(set2))

# Intersection: Return a new sets containing only elements common to both sets

print(set1.intersection(set2))

# Difference : Returns a new set containing elements in the first set but not in the second 

print(set1.difference(set2))

# Symentric difference returns what is not common
print(set1.symmetric_difference(set2))

shop_a_fruits = {'mango', 'pawpaw', 'banana'}
shop_b_fruits = {'banana', 'orange', 'cashew'}
all_fruits = {'mango', 'pawpaw', 'banana', 'orange', 'cashew', 'apple'}


# in check if item is inside

print('mango' in shop_a_fruits)
print('orange' in shop_b_fruits)

# issubset() Returns true if all elements of this set are in the other set 

print(shop_a_fruits.issubset(all_fruits))
print(shop_b_fruits.issubset(all_fruits))

# issubset() check if i get all items of anther set 

print(all_fruits.issuperset(shop_a_fruits))
print(all_fruits.issuperset(shop_b_fruits))

# Isdisjoint() check if there something in common among sets

shop_c_fruits = {'apple', 'grape'}
print(shop_a_fruits.isdisjoint(shop_c_fruits))

print(shop_a_fruits.isdisjoint(shop_b_fruits))

# len returns the number of items in a container 
print(len(shop_a_fruits))

# Dictionary 

fruits_prices = {
    'mango': 500,
    'pawpaw': 800,
    'banana': 300
}

print(fruits_prices)

# getting values from the dictionary 
print(fruits_prices['mango'])

# Add, change and reomove

# Add new fruits
fruits_prices['orange'] = 400
print(fruits_prices)

# change 
fruits_prices['mango'] = 600
print(fruits_prices)

# pop() removes the item with the given key and returns its value

fruits_prices.pop('banana')
print(fruits_prices)

# Clear() removes everything 

#fruits_prices.clear()
print(fruits_prices)

# Keys()

print(fruits_prices.keys())

# Values  bring only the values
print(fruits_prices.values())

# items  bring both keys and value together 

print(fruits_prices.items())

# get safe way to get value

print(fruits_prices.get('mango'))
print(fruits_prices.get('Abualomo'))
