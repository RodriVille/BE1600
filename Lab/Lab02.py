#------------------------------Falling Distance-------------------------------------
def falling_distance(t):
    d = .5 * 9.8 * (t**2)
    return d

seconds = float(input("Enter the falling time for the object in seconds: "))

print("The distance traveled by an object that has fallen for", seconds, "seconds is:", "\n",
        falling_distance(seconds), "meters")

#----------------------------------Future Value--------------------------------------
def future_value(p, i, t):
    f = p * ((1+i/100)**t)
    
    return f

presentVal = float(input("Enter the present value of your account: "))
interestRate = float(input("Enter the interest rate of your account: "))
months = int(input("Enter how many months in the future you want to calculate the value of your account: "))


print("The information for your account is:", "\n",
        "Present value: $", presentVal, "\n",
        "Interest rate: ", interestRate, "%", "\n",
        "After", months, "months, the value of your account will be $", round(future_value(presentVal, interestRate, months), 2))

