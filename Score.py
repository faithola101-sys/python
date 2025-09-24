score1 = int(input("Enter first score (0-100): "))
score2 = int(input("Enter second score (0-100): "))
score3 = int(input("Enter third score (0-100): "))

average = (score1 + score2 + score3) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Average:", average, "Grade:", grade)
