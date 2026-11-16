print("welcome to tip calculator")
bill_Amount = float(input("Enter your amount of bill "))
Tip_percent = float(input("enter tip percent"))
tip_amount = float((Tip_percent/100)*bill_Amount)
final_amount = tip_amount + bill_Amount
print("your final amount is: " , final_amount , "and your tip amount is: " ,tip_amount )