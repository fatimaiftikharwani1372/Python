def gross_salary(basic):
    hra = basic * 20 / 100
    da = basic * 10 / 100
    gross = basic + hra + da

    return hra, da, gross

basic = float(input("Enter basic salary: "))

hra, da, gross = gross_salary(basic)

print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)