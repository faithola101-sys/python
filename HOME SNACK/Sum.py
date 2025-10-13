def parameter(num):
  sum = 0
  for i in range(len(num)):
    num[i] = num[i] ** 2
    sum = sum + num[i]
  return sum


num = [2, 3, 4, 5, 7]
result = parameter(num)
print(result)