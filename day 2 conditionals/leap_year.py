year_to_check = int(input("enter the year you wanna check for the leap year"))
 
if year_to_check % 4 == 0 and year_to_check % 100 != 0 or year_to_check % 400 ==0:
    print("its a leap year")
else :
    print ("its not a leap year")