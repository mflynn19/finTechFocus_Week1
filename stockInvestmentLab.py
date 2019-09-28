### Check the README for additional information ###

# 1. Create a function called number_shares_a() that only accepts an investment amount and returns the number of shares of Fund A which that investment could buy today.
# Then call the function with two different amounts to ensure that it works properly.
def number_shares_a(investment):
    return investment/5.95
print(number_shares_a(300))


# 2. Create a more-general function called number_shares() that takes in an investment amount and a fund. It should return the number of shares of that fund which that investment could buy today.
# Then call the function with different amounts and different funds.
def number_shares(investment, fund):
    if fund.upper() == "A":
        return investment/5.95
    elif fund.upper() == "B":
        return investment/21.01
    elif fund.upper() == "C":
        return investment/23.01
    elif fund.upper() == "D":
        return investment/1.83
    else:
        return "Please try again"
        
print(number_shares(300, "b"))

# 3. Create a more flexible calculator method called history_shares() that takes in an investment amount, fund, and year and returns the number of shares that money could buy in that year.
def history_shares(investment, fund, year):
    if year == 2019:
        if fund.upper() == "A":
            return investment/5.95
        elif fund.upper() == "B":
            return investment/21.01
        elif fund.upper() == "C":
            return investment/23.01
        elif fund.upper() == "D":
            return investment/1.83
        else:
            return "Please try again"
    elif year == 2016:
        if fund.upper() == "A":
            return investment/5.10
        elif fund.upper() == "B":
            return investment/18.08
        elif fund.upper() == "C":
            return investment/19.82
        elif fund.upper() == "D":
            return investment/2.01
        else:
            return "Please try again"
    elif year == 2012:
        if fund.upper() == "A":
            return investment/4.10
        elif fund.upper() == "B":
            return investment/15.76
        elif fund.upper() == "C":
            return investment/11.15
        elif fund.upper() == "D":
            return investment/1.45
        else:
            return "Please try again"
    elif year == 1996:
        if fund.upper() == "A":
            return investment/3.75
        elif fund.upper() == "B":
            return investment/14.10
        elif fund.upper() == "C":
            return investment/8.03
        elif fund.upper() == "D":
            return investment/1.22
        else:
            return "Please try again"
    elif year == 1980:
        if fund.upper() == "A":
            return investment/2.50
        elif fund.upper() == "B":
            return investment/12.02
        elif fund.upper() == "C":
            return investment/0.63
        elif fund.upper() == "D":
            return investment/1.22
        else:
            return "Please try again"
    else:
        return "Please try again"
        
print(history_shares(300, "b", 1980))


### Advanced Bonus Challenge ###

# 4. What is the change of an investment over time? Create a method calculate_profit() that accepts an initial investment amount, the fund, and the initial investment year, and returns the current profit made on the initial investment. This is an open ended one - there are many ways to do this!
def calculate_profit(investment, fund, year):
    if year == 2019:
        if fund.upper() == "A":
            return investment
        elif fund.upper() == "B":
            return investment
        elif fund.upper() == "C":
            return investment
        elif fund.upper() == "D":
            return investment
        else:
            return "Please try again"
    elif year == 2016:
        if fund.upper() == "A":
            shares = investment/5.10
            profit = shares * 5.95
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "B":
            shares = investment/18.08
            profit = shares * 21.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "C":
            shares = investment/19.82
            profit = shares * 23.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "D":
            shares = investment/2.01
            profit = shares * 1.83
            return "$" + str(round(profit - investment, 2)) 
        else:
            return "Please try again"
    elif year == 2012:
        if fund.upper() == "A":
            shares = investment/4.10
            profit = shares * 5.95
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "B":
            shares = investment/15.76
            profit = shares * 21.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "C":
            shares = investment/11.15
            profit = shares * 23.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "D":
            shares = investment/1.45
            profit = shares * 1.83
            return "$" + str(round(profit - investment, 2)) 
        else:
            return "Please try again"
    elif year == 1996:
        if fund.upper() == "A":
            shares = investment/3.75
            profit = shares * 5.95
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "B":
            shares = investment/14.10
            profit = shares * 21.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "C":
            shares = investment/8.03
            profit = shares * 23.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "D":
            shares = investment/1.22
            profit = shares * 1.83
            return "$" + str(round(profit - investment, 2)) 
        else:
            return "Please try again"
    elif year == 1980:
        if fund.upper() == "A":
            shares = investment/2.50
            profit = shares * 5.95
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "B":
            shares = investment/12.02
            profit = shares * 21.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "C":
            shares = investment/0.63
            profit = shares * 23.01
            return "$" + str(round(profit - investment, 2)) 
        elif fund.upper() == "D":
            shares = investment/1.22
            profit = shares * 1.83
            return "$" + str(round(profit - investment, 2)) 
        else:
            return "Please try again"
    else:
        return "Please try again"

print(calculate_profit(2000, "d", 1996))


# Bonus: Format the output of the function as USD currency, so instead of 1000, the function should output $1000.00.



### Double Advanced Bonus Challenge ###

# 5. Which investment is the best? Create a method best_choice() that accepts an investment amount and a year, and returns the name of the fund that would have made the most money for the investor.



# Bonus: In addition to the name of the fund, also return how much money the investor would have earned.



### Triple Advanced Bonus Challenge ###

# 6. Consider the current profit difference between making an investment in a fund several years apart. Create a method investment_diff() that accepts an investment amount, a fund, and two year values and returns the current profit difference if the money had been made earlier vs. later.



# Bonus: How can you account for a sloppy investment advisor who puts the years in a different order than you expect?


