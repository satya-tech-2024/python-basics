to_hours = 24
unit = "hours"


def get_hours(day):
    return f"{day} contains {int(day) * to_hours} {unit}"


input_value = input("Enter number of days: ")
# if input_value.isdigit():
#     print(get_hours(int(input_value)))
# else:
#     print("Invalid input")

try:
    print(get_hours(input_value))
except ValueError:
    print("Invalid data")

