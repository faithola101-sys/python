
header = "number\tsquare\tcube"


print(header)


for number in range(1, 6):
   
    square = number ** 2
    cube = number ** 3
    
   
    print(f"{number}\t{square}\t{cube}")