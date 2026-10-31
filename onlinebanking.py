# Online Banking Transaction System

class InsufficientBalanceError(Exception):
    pass

try:
    balance = 5000

    print("Current Balance:", balance)

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance!")

except ValueError as e:
    print("Invalid Input:", e)

except InsufficientBalanceError as e:
    print("Transaction Failed:", e)

else:
    balance = balance - amount
    print("Withdrawal successful!")
    print("Remaining Balance:", balance)

finally:
    print("Thank you for using our banking system.")
