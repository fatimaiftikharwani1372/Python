numbers = list(range(1, 21))
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
     even += 1
    else:
     odd += 1
print("Created List:", numbers)
print("Number of Even Elements:", even)
print("Number of Odd Elements:", odd)