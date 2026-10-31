cart = []
n = int(input("Enter the number of items you want to add to the cart: "))
for i in range(n):
    item= input("Enter the name of items:")
    cart.append(item)
print("Item added to cart:")
for item in cart:
    print(item)

                