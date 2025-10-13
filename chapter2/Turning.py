problem = input("Whats your problem? ")
enter = input("Press enter")
print(problem)

problem = input("Have you had this problem before(yes or no)? ")
print(problem)

if problem.lower() == "yes":
 print('Well, you have it again.')

else:
 print('Well, you have it now.')
