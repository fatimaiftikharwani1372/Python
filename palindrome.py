text = input("Enter a string: ")
reverse = ""
length = len(text)
for i in range(length - 1, -1, -1):
 reverse = reverse + text[i]
print("Original String:", text)
print("Reversed String:", reverse)
if text == reverse:
 print("The string is a Palindrome")
else:
 print("The string is not a Palindrome")