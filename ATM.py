print("ATM Withdrawal System")

while True:
    amount = int(input("Enter amount: "))

    if amount == 0:
        break

    if amount < 0:
        print("Invalid Amount")
        continue

    if amount > 10000:
        pass

    print("Withdrawal amount: $", amount)

print("\nThank you for using the ATM!")
