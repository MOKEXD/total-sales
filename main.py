from sisepuede import init
from total import calculate_total_sales
from datetime import datetime
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
print("===========================================")
print("        hello welcome to moke app          ")
print("===========================================")
print("Date:", date)
print("Time:", time)
init()
calculate_total_sales()
