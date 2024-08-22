numbers = [3, 6, 79, 12, 2, 9, 45]

max = numbers[0]

for number in numbers:
    if number > max:
        max = number

print(f"Max is {max}")