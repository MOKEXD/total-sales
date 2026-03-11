#this file have a function to calculate the total sales of the day, importing products from sisepuede.py

from sisepuede import products

def calculate_total_sales(): #here we create a function to calculate the total sales of the day
    total_day = 0

    for product in products:
        totalsales = product["price"] * product["quantity"]
        print("total sales:", totalsales)
        total_day += totalsales

    print("total day sales:", total_day)
