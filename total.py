from sisepuede import products

def calculate_total_sales():
    total_day = 0

    for product in products:
        totalsales = product["price"] * product["quantity"]
        print("total sales:", totalsales)
        total_day += totalsales

    print("total day sales:", total_day)