print(f"{'number':>5} {'square':>5} {'cube':>5}")

for num in range(0, 6):       
    square = num * num          
    cube = square * num
    print(f"{num:<6}{square:<8}{cube:<10}")
