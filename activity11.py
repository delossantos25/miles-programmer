temp = input("Enter a temperature --> ")

if temp.isnumeric:
    if eval(temp) <= 0:
        print("The temperature is consider Below Freezing")
    elif eval(temp) >= 1 and eval(temp) <= 15:
        print("The temperature is Consider Extreme Cold")
    elif eval(temp) >= 16 and eval(temp) <= 30:
        print("The temperature is consider Cold")
    elif eval(temp) >= 31 and eval(temp) <= 38:
        print("The temperature is consider Lukewarm")
    elif eval(temp) >= 39 and eval(temp) <= 42:
        print("The temperature is consider Warm")
    elif eval(temp) >= 43 and eval(temp) <= 50:
        print("The temperature is consider Hot ")
    elif eval(temp) >= 51 and eval(temp) <= 60:
        print("The temperature is consider Extremely Hot")
    elif eval(temp) >= 60:
        print("The temperature is consider Burning")
else:
    print("Invalid Temperature")