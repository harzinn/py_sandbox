def computepay(h,r):
    # error checking when converting to floats
    try:
        fHours = float(h)
    except:
        fHours = -1
    try:
        fRate = float(r)
    except:
        fRate = -1
    
    otRate = fRate * 1.5
    otHours = fHours - 40

    if fHours <= 40:
        return fRate * fHours
    else:
        otPay = otHours * otRate
        return (40 * fRate) + otPay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

p = computepay(hrs,rate)
print("Pay",p)
