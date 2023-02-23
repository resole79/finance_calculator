"""

For this task, assume that you have been approached by a small financial
company and asked to create a program that allows the user to access two
different financial calculators: an investment calculator and a home loan
repayment calculator.
Create a new Python file in this folder called finance_calculators.py.
At the top of the file include the line:
import math
Write the code that will do the following:
1.The user should be allowed to choose which calculation they want to do.
The first output that the user sees when the program runs should look like
this :
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:
2.How the user capitalises their selection should not affect how the
program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’,
‘INVESTMENT’, etc., should all be recognised as valid entries. If the user
doesn’t type in a valid input, show an appropriate error message.
3.If the user selects ‘investment’, do the following:
Ask the user to input:
The amount of money that they are depositing.
The interest rate (as a percentage). Only the number of the interest
rate should be entered — don’t worry about having to deal with the
added ‘%’, e.g. The user should enter 8 and not 8%.
The number of years they plan on investing.
Then ask the user to input if they want “simple” or “compound”
interest, and store this in a variable called interest. Depending on
whether or not they typed “simple” or “compound”, output the
appropriate amount that they will get back after the given period,
at the specified interest rate. See below for the formula to be used:
Interest formula:
The total amount when simple interest is applied is calculated as
follows: 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
The Python equivalent is very similar: A =P *(1 + r*t)
The total amount when compound interest is applied is calculated as
follows: 𝐴 = 𝑃(1 + 𝑟)
𝑡
The Python equivalent is slightly different: A = P * math.pow((1+r),t)
In the formulae above:
‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
then r is 0.08.
‘P’ is the amount that the user deposits.
‘t’ is the number of years that the money is being invested.
‘A’ is the total amount once the interest has been applied.
Print out the answer!
Try entering 20 years and 8 (%) and see what the difference is
depending on the type of interest rate!
4. If the user selects ‘bond’, do the following:
Ask the user to input:
The present value of the house. e.g. 100000
The interest rate. e.g. 7
The number of months they plan to take to repay the bond. e.g. 120
Bond repayment formula:
The amount that a person will have to be repaid on a home loan each
month is calculated as follows: 𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 =𝑖 ×𝑃 / 1− (1+𝑖)−𝑛
The Python equivalent is slightly different:
repayment = (i * P)/(1 - (1 + i)**(-n))
In the formula above:
‘P’ is the present value of the house.
‘i’ is the monthly interest rate, calculated by dividing the annual
interest rate by 12. Remember to divide the interest entered by
the user by 100 e.g. (8 / 100) before dividing by 12.
‘n’ is the number of months over which the bond will be repaid.
Calculate how much money the user will have to repay each month
and output the answer

"""
import math

# Explain user whats is "investment" and "bond". Ask user a choice
print ("investment - to calculate the amount of interest you'll earn on your investment")
print ("bond -       to calculate the amount you'll have to pay on a home loan")
financial_choice = input ("\nEnter either 'investment' or 'bond' from the menu above to proceed : ")

# If choice is "investment" the user need to insert :
# "money_deposit" (how much money you want to invest)
# "interest_rate_investment" (the percent of your rate)
# "number_of_years_invest" (how many year you want to invest)
#
if financial_choice.lower() == "investment" :
    money_deposit = float(input ("\nPlease, enter the amount of money that you are depositing : "))
    interest_rate_investment = float(input ("Please, enter the interest rate : "))
    number_of_years_invest = int(input ("Please, enter the number of years you plan on investing : "))
    interest = input ("Please, enter you want “simple” or “compound” interest? : ")

    # If choice simple investment need to calculate the formula below and print out the result
    # simple interest A =P *(1 + r*t)
    # ‘r’ is the interest entered above divided by 100, e.g. if 8 % is entered, then r is 0.08.
    # ‘P’ is the amount that the user deposits.
    # ‘t’ is the number of years that the money is being invested.
    # ‘A’ is the total amount once the interest has been applied.

    if interest.lower() == "simple" :
        simple_interest = money_deposit * (1 + ((interest_rate_investment / 100) * number_of_years_invest))
        print(f"\nYour simple interest is : {round(simple_interest, 2):.2f}")

    # If choice compound investment need to calculate the formula below and print out the result
    # compound interest A = P * math.pow((1+r),t)
    # ‘r’ is the interest entered above divided by 100, e.g. if 8 % is entered, then r is 0.08.
    # ‘P’ is the amount that the user deposits.
    # ‘t’ is the number of years that the money is being invested.
    # ‘A’ is the total amount once the interest has been applied.

    elif interest.lower() == "compound" :
        compound_interest = money_deposit * math.pow((1+(interest_rate_investment / 100)), number_of_years_invest)
        print(f"\nYour compound interest is : {round(compound_interest, 2):.2f}")

    else :
        print ("Sorry, your choice is incorrect!")

# If choice is "bond" the user need to insert :
# "value_of_house" (the value of your house)
# "interest_rate_bond" (the percent of your rate)
# "number_of_months_repay" (how many month do you want to repay)

elif financial_choice.lower() == "bond" :
    value_of_house = float(input ("Please, enter the present value of the house : "))
    interest_rate_bond = float(input ("Please, enter the interest rate : "))
    number_of_months_repay = int(input ("Please, enter the number of months you plan to take to repay the bond : "))

    # Calculate the formula below and print out the result
    # repayment = (i * P) / (1 - (1 + i) ** (-n))
    # ‘P’ is the present value of the house.
    # ‘i’ is the monthly interest rate, calculated by dividing the annual
    # interest rate by 12. Remember to divide the interest entered by
    # the user by 100 e.g. (8 / 100) before dividing by 12
    # ‘n’ is the number of months over which the bond will be repaid

    i = ((interest_rate_bond / 100) / 12)
    repayment = (i * value_of_house) / (1 - (1 + i) ** (-number_of_months_repay))
    print(f"\nYour repayment is : {round(repayment, 2):.2f}")

else :
    print ("Sorry, your choice is incorrect!")
