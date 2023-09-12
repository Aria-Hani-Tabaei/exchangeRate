import requests
from time import sleep

site = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=59052221af72b22fc81501b9c2f4659b")

information = site.json()['rates']

for name in information:
    print(name + ", ", end="")

# to make a line from the inquiries
print()

sell = input("What is the currency you want to sell:").upper()
number = float(input("how many do you want to sell:"))
buy = input("What is the currency you want to buy:").upper()

if sell == "LIRA":
    sell = "TRY"
elif sell == "DOLLAR":
    sell = "USD"
elif sell == "RIAL":
    sell = "IRR"

if buy == "LIRA":
    buy = "TRY"
elif buy == "DOLLAR":
    buy = "USD"
elif buy == "RIAL":
    buy = "IRR"

get = "{:.2f}".format(information[buy] / information[sell] * number)

print(f"you should get {get} {buy}")

sleep(10)