def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y
def main():
    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '5':
            print("Exited")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please choose a number from 1 to 5.")
            continue
        num1 = input("Enter first number: ")
        if not num1.replace('.', '', 1).isdigit():
            print("Invalid input! Please enter a valid number.")
            continue
        num2 = input("Enter second number: ")
        if not num2.replace('.', '', 1).isdigit():
            print("Invalid input! Please enter a valid number.")
            continue
        num1 = float(num1)
        num2 = float(num2)
        if choice == '4' and num2 == 0:
            print("Error: Cannot divide by zero!")
            continue
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
if __name__ == "__main__":
    main()
