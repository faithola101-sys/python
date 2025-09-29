
number = int(input("Enter a five-digit integer: "))

num_digits = 5  

divisor = 10 ** (num_digits - 1)  

for i in range(num_digits):
    digit = number // divisor     
    print(digit, end=" ")
    number = number % divisor      
    divisor //= 10                 

print()  
