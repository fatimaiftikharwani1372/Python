def calculate_area(length, breadth):
    area = length * breadth
    return area

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

result = calculate_area(length, breadth)

print("Length:", length)
print("Breadth:", breadth)
print("Area of rectangle:", result)