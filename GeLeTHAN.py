numbers = [5, 12, 8, 20, 15, 3, 18, 10]
greater = 0
less_equal = 0
for num in numbers:
 if num > 10:
    greater = greater + 1
 else:
    less_equal = less_equal + 1
print("List:", numbers)
print("Numbers greater than 10:", greater)
print("Numbers less than or equal to 10:", less_equal)