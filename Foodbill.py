def Calculate_bill(amount):
    gst = amount * 0.5
    service_charge = amount * 0.10
    final_bill = amount + gst + service_charge
    return gst, service_charge, final_bill

customer_name = input("Enter customer name: ")
food_bill = float(input("Enter food bill amount: "))

gst, service_charge, final_bill = Calculate_bill(food_bill)

print("\n---Food Bill Details---")
print("Customer Name:", customer_name)
print("Food Bill Amount: Rs.", food_bill)
print("GST: Rs.", gst)
print("Service Charge: Rs.", service_charge)
print("Final Bill Amount: Rs.", final_bill)
