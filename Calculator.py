def power(base, exp):
    result = 1
    for _ in range(abs(exp)):
        result *= base
    return result if exp >= 0 else 1 / result

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sine(x):
    x = x % (2 * 3.141592653589793)  # Reduce angle
    result, term, n = 0, x, 1
    while abs(term) > 1e-10:
        result += term
        term *= -1 * x**2 / ((2*n)*(2*n+1))
        n += 1
    return result

def cosine(x):
    x = x % (2 * 3.141592653589793)  # Reduce angle
    result, term, n = 1, 1, 1
    while abs(term) > 1e-10:
        term *= -1 * x**2 / ((2*n-1)*(2*n))
        result += term
        n += 1
    return result

def tangent(x):
    cos_value = cosine(x)
    if abs(cos_value) < 1e-10:
        return "Undefined (tan(x) approaches infinity)"
    return sine(x) / cos_value

def log(x):
    if x <= 0:
        return "Undefined (log(x) for x <= 0)"
    result, term, n = 0, (x - 1) / (x + 1), 1
    while abs(term) > 1e-10:
        result += term / (2*n - 1)
        term *= ((x - 1) / (x + 1))**2
        n += 1
    return 2 * result

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Sine (sin)")
    print("7. Cosine (cos)")
    print("8. Tangent (tan)")
    print("9. Logarithm (log)")
    print("10. Exit")
    
    while True:
        try:
            choice = input("\nEnter the operation number (1-10): ")
            
            if choice == '10':
                print("Exiting the calculator. Goodbye!")
                break
            
            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero!")
                elif choice == '5':
                    exp = int(num2)
                    print(f"The result is: {power(num1, exp)}")
            
            elif choice == '6':
                angle = float(input("Enter the angle in radians: "))
                print(f"The result is: {sine(angle)}")
            
            elif choice == '7':
                angle = float(input("Enter the angle in radians: "))
                print(f"The result is: {cosine(angle)}")
            
            elif choice == '8':
                angle = float(input("Enter the angle in radians: "))
                print(f"The result is: {tangent(angle)}")
            
            elif choice == '9':
                num = float(input("Enter the number: "))
                print(f"The result is: {log(num)}")
            
            else:
                print("Invalid choice! Please try again.")
        
        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
