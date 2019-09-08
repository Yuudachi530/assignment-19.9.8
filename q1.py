Weighting = 10
Total = 0
Count = 1
while True:
    Digit = eval(input("enter the digit: "))
    Value = Digit * Weighting
    Total = Total + Value
    if Count == 9:
        break
    else:
        Count = Count + 1
Remainder = Total % 11
CheckDigit = 11 - Remainder
if CheckDigit == 10:
    CheckDigit = Total

