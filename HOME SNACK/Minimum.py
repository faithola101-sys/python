def minimum(num):
    minimum = num[3]
    for i in range(len(num)):
       
        if num[i] < minimum:
           minimum = num[i]
    return minimum

num = [8,4,9,2,5,7,3]   
result = minimum(num)
print(result)