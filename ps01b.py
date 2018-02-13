# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:19:25 2018

@author: RedoxR
"""


#annual_salary = float(input('Enter your annual salary: '))
#portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
#total_cost = float(input('Enter the cost of your dream home: '))
#semi_annual_raise = float(input('Enter the semi-annual raise: '))
#
#portion_down_payment = total_cost*float(0.25)
#
#month_counter = 0
#
#current_savings = 0
#while current_savings < portion_down_payment:
#    current_savings += ((portion_saved*annual_salary)/12) + ((current_savings*0.04)/12)
#    month_counter += 1
#    if month_counter%6 == 0:
#        annual_salary = semi_annual_raise*annual_salary + annual_salary
#print('Number of months: ' + str(month_counter))

annual_salary = float(input('Enter your annual salary: '))
monthly_salary = annual_salary/12
semi_annual_raise = 0.07
investment_return_annual = 0.04
investment_return_monthly = investment_return_annual/12
down_payment = 0.25
total_cost = 1000000

required_cost = down_payment*total_cost

total_salary = 0
epsilon = 0.01
num_guesses = 0
low = 0
high = 10000
guess = (high + low)/2.0
for i in range(0,36):
    if i%6 == 0 and i != 0:
        monthly_salary += monthly_salary*semi_annual_raise
    monthly_salary += monthly_salary*investment_return_monthly
    total_salary += monthly_salary 
if total_salary < required_cost:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs(total_salary*guess - required_cost) >= epsilon:
        if total_salary*guess < required_cost:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        num_guesses += 1
    print('Best savings rate: ' + str(guess))
    print('Amount of iterations: ' + str(num_guesses))
    
  

