try:
    hours = int(input("Enter hours: "))
    rate = int(input("Enter rate: "))
    hours = float(hours)
    rate = float(rate)
    if hours>40:
        pay_above = (hours-40) * (rate*1.5)
        pay = 40 * rate
        pay = pay+pay_above
    else:
        pay = hours * rate
    print(f"Pay ${pay}")
except:
    print("\nError, please enter a numeric input")