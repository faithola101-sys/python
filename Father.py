// collect the age of the father 
   collcect the age of the son
   subtract the fathers age from the twice the sons age //

father_age = int(input("Enter father's age (1-80): "))
son_age = int(input("Enter son's age (1-80): "))

years = abs(father_age - 2 * son_age)
print("The father was/will be twice as old in", years, "years.")
