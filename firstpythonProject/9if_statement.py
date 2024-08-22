# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("Its a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("Its a cold day")
#     print("Wear warm clothes")
# else:
#     print("Its a lovely day")
# print("Enjoy your day!")

house_price = 1000000
has_good_credit = True
has_fair_credit = True

if has_good_credit:
    down_payment = 0.1 * house_price
elif has_fair_credit:
    down_payment = 0.15 * house_price
else:
    down_payment = 0.2 * house_price

print(f"The down payment for this house is ${down_payment}")
