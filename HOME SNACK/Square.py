def parameter(num):

  for i in range(len(num)):
    num[i] = num[i] ** 2
  return num

num = [2, 3, 4, 5, 7]
result = parameter(num)
print(result)