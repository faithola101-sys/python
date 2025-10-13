row = 8

for i in range(1, row + 1):   
    for j in range(i):        
        print("*", end=" ")
    print()   
print()

for i in range(1, row + 1):   
    for j in range(i):        
        print(" ", end=" ")
    for k in range(row - i + 1):        
        print("*", end=" ")
    print()   
print()

for i in range(1, row + 1):   
    for k in range(row - i + 1):        
        print(" ", end=" ")
    for j in range(i):        
        print("*", end=" ")
    print()   
print()

for i in range(1, row + 1):   
    for k in range(row - i + 1):        
        print("*", end=" ")
    for j in range(i):        
        print(" ", end=" ")
    print()   
print()