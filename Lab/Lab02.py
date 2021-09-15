#Falling Distance
def falling_distance(t):
    distance= .5 * 9.8 * (t**2)
    print("The distance traveled by an object that has fallen for", t, "seconds is:", "\n", distance, "meters")

time = float(input("Enter the falling time for the object: "))

falling_distance(time)

#Future Value
def future_value(p, i, t):
    f = p * ((1+i/100)**t)
    print("The information for your account is:", "\n",
          "Present value: $", p, "\n",
          "Interest rate: ", i, "%", "\n",
          "After", t, "months, the value of your account will be $", f)
    
presentVal = float(input("Enter the present value of your account: "))
interestRate = float(input("Enter the interest rate of your account: "))
time = int(input("Enter the time you want to calculate the value of your account of: "))

future_value(presentVal, interestRate, time)