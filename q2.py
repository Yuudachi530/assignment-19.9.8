Count_Positive = 0
Count_Negative = 0

while True:
    Number = eval(input("enter a number: "))
    if Number > 0:
        Count_Positive = Count_Positive + Number
    elif Number < 0:
        Count_Negative = Count_Negative + Number
    else:
        break
print()
print("sum of positive: ",Count_Positive)
print("sum of negative: ",Count_Negative)
