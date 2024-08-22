print('Satya')

# Wrong
# print('Satya is '+45 + "year old")

# Correct
print('Satya is '+ str(45) + "year old")
print(f"He was born in {1979}")

to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_seconds(day):
    print(f"{day} day(s) are {day * to_seconds} {name_of_unit}")

# print(f"One day is  {24 * 60 * 60} {name_of_unit}")
# print(f"10 days are {10 * to_seconds} {name_of_unit}")


days_to_seconds(1)
days_to_seconds(10)
days_to_seconds(30)

# days = int(input("Enter number days "))
days = eval(input("Enter number days "))
days_to_seconds(days)
