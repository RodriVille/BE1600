sales = float(input("Enter the total sales for the month: "))

def tax(s):
    stateTax = s * .04
    countyTax = s * .02
    totalTax = stateTax + countyTax
    
    print("Monthly sales: $", s, "\n",
          "State tax: $", stateTax, "\n",
          "County tax: $", countyTax, "\n",
          "Total tax: $", totalTax)

tax(sales)