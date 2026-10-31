def count_characters(text):
    letters = 0
    digits = 0

    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            letters = letters + 1
        elif ch >= 'a' and ch <= 'z':
            letters = letters + 1
        elif ch >= '0' and ch <= '9':
            digits = digits + 1

    return letters, digits


text = input("Enter a string: ")

letters, digits = count_characters(text)

print("String:", text)
print("Number of letters:", letters)
print("Number of digits:", digits)