print("Welocome to Tip Calculator")
totalbill= float(input("What was the total bill?$"))
tip= int(input("what pecentage tip you would like to give?12,15,18?"))
split = int(input ("how many people to split the bill?  "))

tip_percentage = (totalbill * tip) / 100
grand_total_bill= totalbill+tip
per_personpay = (grand_total_bill/split)
print(f"Each person should pay ${round(per_personpay,2)}")