RogueValue = -1
Total = 0
Count = 0
Number = eval(input("enter a number: "))
while Number != RogueValue:
    Count = Count + 1
    Total = Total + Number
    Number = eval(input("enter a number: "))
if Count > 0:
    Average = Total / Count
    print(Average)
