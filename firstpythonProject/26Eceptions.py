try:
    age = int(input("Enter your age: "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print('Invalid Value')
