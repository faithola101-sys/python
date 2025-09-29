
    result = 1
    i = 1            
    while i <= n:    
        result *= i
        i += 1
    return result


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Error: Please enter a number that is not negative.")
else:
    print(f"The factorial of {number} is {factorial(number)}")




