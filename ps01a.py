# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:19:25 2018

@author: RedoxR
"""


annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise: '))

portion_down_payment = total_cost*float(0.25)

month_counter = 0

current_savings = 0
while current_savings < portion_down_payment:
    current_savings += ((portion_saved*annual_salary)/12) + ((current_savings*0.04)/12)
    month_counter += 1
    if month_counter%6 == 0:
        annual_salary = semi_annual_raise*annual_salary + annual_salary
print('Number of months: ' + str(month_counter))


     

