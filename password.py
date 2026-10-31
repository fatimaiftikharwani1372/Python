import re

print("Fatima Wani")
email = "student@gmail.com"
phone = "9999999999"
password = "Student123"

if re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email):
    print("Email: Valid")
else:
    print("Email: Invalid")

if re.match(r'^[0-9]{10}$', phone):
    print("Phone Valid")
else:
    print("Phone: Invalid")

text = "Contact us at student@gmail.com and stud@gmail.com"
result = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
print("Email found:", result)

data = "Python,Java,C++"
languages = re.split(r',', data)
print("Languages:", languages)

text = "My phone number is 9876543210"
result = re.sub(r'[0-9]', '*', text)
print("After replacement:", result)