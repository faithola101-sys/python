num = 0
total = 0
product = 1
largest = num
smallest = num


for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    
    total += num
    product *= num
    
  
    if num > largest:
       largest = num
    
   
    elif num > smallest:
         smallest = num


average = total / 4


print("Sum:", total)
print("Product:", product)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)