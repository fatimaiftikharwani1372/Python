def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    return total, percentage, grade


m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

total, percentage, grade = calculate_result(m1, m2, m3)

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)