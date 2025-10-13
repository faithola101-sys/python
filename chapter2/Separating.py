
number = int(input("Enter a five-digit number: "))

divisor = 100000  

for i in range(6):
    digit = number // divisor   
    print(digit, end="  ")      
    number = number % divisor   
    divisor //= 10 
