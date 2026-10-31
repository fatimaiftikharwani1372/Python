def count_vowels(text):
    count = 0

    for i in range(len(text)):
        ch = text[i]

        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count = count + 1
        elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            count = count + 1

    return count

text = input("Enter a string: ")
result = count_vowels(text)

print("String:", text)
print("Total number of vowels:", result)