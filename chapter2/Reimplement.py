

numbers = []  

for i in range(4):
    value = int(input(f"Enter integer {i+1}: "))
    numbers.append(value)


total = sum(numbers)
average = total / len(numbers)
product = 1
for n in numbers:
    product *= n

smallest = min(numbers)
largest = max(numbers)


print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
