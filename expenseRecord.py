# Create and write expense records
print("Name: Fatima Wani")

with open("expenses.txt", "w") as file:
    file.write("Food,150\n")
    file.write("Travel,80\n")
    file.write("Stationary,100\n")

import os

# Check if file exists
if os.path.exists("expenses.txt"):
    print("File exists")
else:
    print("File does not exist")

# Rename the file
os.rename("expenses.txt", "my_expenses.txt")

# Get file size
size = os.path.getsize("my_expenses.txt")
print("File Size:", size, "bytes")

try:
    with open("my_expenses.txt", "r") as file:
        total = 0
        count = 0

        print("\nExpense Records")

        for line in file:
            data = line.strip().split(",")

            item = data[0]
            amount = float(data[1])

            print(item, "-", amount)

            total = total + amount
            count = count + 1

        print("\nTotal Expenditure:", total)
        print("Number of Records:", count)

except OSError:
    print("File does not exist")