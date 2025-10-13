
def maximum(num):
    maximum = num[2]
    for i in range(len(num)):
       
        if num[i] < maximum:
           maximum = num[i]
    return maximum

num = [8,4,9,2,5,7,3]   
result = maximum(num)
print(result)