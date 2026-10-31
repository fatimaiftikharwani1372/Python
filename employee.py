name = input("Enter Employee Name: ")
salary = float(input("Enter Monthly Salary: "))
rating = int(input("Enter Performance Rating (1-5): "))

if rating == 5:
    bonus = salary * 0.20
    level = "Excellent"
elif rating == 4:
    bonus = salary * 0.15
    level = "Very Good"
elif rating == 3:
    bonus = salary * 0.10
    level = "Good"
elif rating == 2:
    bonus = salary * 0.05
    level = "Average"
elif rating == 1:
    bonus = 0
    level = "Poor"
else:
    print("Invalid Rating!")
    exit()

final_salary = salary + bonus

print("\nEmployee Name:", name)
print("Performance Level:", level)
print("Bonus:", bonus)
print("Final Salary:", final_salary)
