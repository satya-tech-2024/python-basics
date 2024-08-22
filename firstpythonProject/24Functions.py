def greet_user(first_name, last_name = '' ):
    print(f"Hello {first_name} {last_name}")

def square(number):
    return number * number

greet_user('Satya')
greet_user('Subha', 'Josyula') #positional arguments
greet_user(last_name='Subha', first_name = 'Josyula') #keyword arguments

print(square(square(3)))

#By default, all functions return None