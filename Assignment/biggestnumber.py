# Loop throgh a list and print out the biggest number 

numbers = [12, 45, 7, 89, 230, 56]
biggest = numbers[0]

for n in numbers:
    if n > biggest:
        biggest = n

print(f"The biggest number is: {biggest}")
    