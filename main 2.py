num1 = float(input("Enter the first number: "))
print()

num2 = float(input("Enter the second number: "))
print()

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
choice = input("Choose the operation: ")
print()

if choice == "1":
    print(f"It is: {num1 + num2}")
    
elif choice == "2":
    print(f"It is: {num1 - num2}")
    
elif choice == "3":
    print(f"It is: {num1 * num2}")
    
elif choice == "4":
    while num2 == 0:
        print("You can't divide by 0!")
        num2 = float(input("Please enter a different second number: "))
    print(f"It is: {num1 / num2}")
        
else:
    print("Invalid Operation")
    