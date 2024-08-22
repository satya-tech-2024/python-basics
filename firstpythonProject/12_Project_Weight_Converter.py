weight = input("Enter your weight: ")
unit = input(" (L)b or (K)g: ")
if unit.upper() == "L":
    converted = float(weight) * 0.45
    print(f"Your Weight is {converted} kilos")
else:
    converted = float(weight) / 0.45
    print(f"Your Weight is {converted} pounds")