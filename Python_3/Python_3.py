number = int(input("Enter an integer: "))

if number == 0:
    print("The number is 0")
else:
    if number < 0:
        sign = "negative"
    else:
        sign = "positive"
        
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "uneven"

    print(sign, parity, "number")