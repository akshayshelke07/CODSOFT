print("🤗==== Welcome to My Calculator ====🤗")

# Get first number 
first_input = input("Enter the first number: ")
try:
    num1 = float(first_input)
except ValueError:
    print("Oops! That's not a valid number.")
    exit()

# Get second number
second_input = input("Enter the second number: ")
try:
    num2 = float(second_input)
except ValueError:
    print("Oops! That's not a valid number.")
    exit()


print("\nWhat would you like to do?")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter 1/2/3/4: ")


if choice == '1':
    result = num1 + num2
    symbol = '+'
elif choice == '2':
    result = num1 - num2
    symbol = '-'
elif choice == '3':
    result = num1 * num2
    symbol = '*'
elif choice == '4':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num1 / num2
    symbol = '/'
else:
    print("Invalid choice. Please select from 1 to 4.")
    exit()

# Print result
print(f"\nResult: {num1} {symbol} {num2} = {result}")
print("Thanks for using my calculator!")
