num = [2,3,4,6,7,8]

for i in range(len(num)):
   
   largest = 8
   smallest = 2

   if(largest < num[i]):
    num[i] = largest
   
   if(smallest > num[i]):
    num[i] = smallest

print(f"The largest is {largest} & smallest is {smallest}")