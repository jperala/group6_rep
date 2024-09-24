miles = float(input("Please enter miles: "))
print("\n")
gallons = float(input("Please enter gallons: "))
def mpgcalc(miles,gallons):
    mpg=round((miles/gallons),4)
    #print(mpg)
    return mpg
print("The average miles miles per gallon is : ",mpgcalc(miles,gallons))
