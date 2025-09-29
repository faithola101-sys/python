days = ["monday","tuesday","wednesday","thurday","friday","saturday"]
for day in days:
 print(day)

numbers = [1,2,3,4,5,6,7]
for number in numbers:
 print(number)

for number, day in zip(numbers, days):

  print(f"{number}. {day}")