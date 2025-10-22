def daily_wages(tdp):
   

    base_pay = 5000
    
    if tdp < 0 or tdp > 100:
        raise ValueError("only 0 to 100 delivery is valid")

    if tdp < 50:
        amount_per_parcel = 160
    elif 50 <= tdp <= 59:
        amount_per_parcel = 200
    elif 60 <= tdp <= 69:
        amount_per_parcel = 250
    elif 70 <= tdp <= 100:
        amount_per_parcel = 500
   
        
    daily_wages = tdp * amount_per_parcel + base_pay
    return daily_wages

print(daily_wages(80))

