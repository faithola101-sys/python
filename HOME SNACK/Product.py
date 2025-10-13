num = [20, 12, 11, 12, 5, 9, 8]

product = 1

for i in range(1, len(num) + 1):
  
  if(i % 3 == 0):
  
     product = product * num[i]
    
     

print(product)