num = int(input("Enter three number: "))

digit1 = (num // 1000) % 10
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10

sum = digit1 + digit2 + digit3
average = sum / 3
product = digit1 * digit2 * digit3

if digit1 > digit2 and digit1 > digit3:
    print(digit1, "is the highest")
    if digit2 < digit3:
        print(digit2, "is the lowest")
    else:
        print(digit3, "is the lowest")

elif digit2 > digit1 and digit2 > digit3:
    print(digit2, "is the highest")
    if digit1 < digit3:
        print(digit1, "is the lowest")
    else:
        print(digit3, "is the lowest")

else:
    print(digit3, "is the highest")
    if digit1 < digit2:
        print(digit1, "is the lowest")
    else:
        print(digit2, "is the lowest")
print("Sum:", sum)
print("Average:", average)
print("Product:", product)