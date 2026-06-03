import json
from urllib.request import urlopen

with urlopen("https://api.exchangerate-api.com/v4/latest/USD") as response:
    source = response.read()


data = json.loads(source)

print(json.dumps(data, indent = 2))

# print(len(data['rates']))

def usd_converter(country_code, amt):
    for key, value in data['rates'].items():
        if (key == country_code.upper()):
            print("Exchange rate:", value)
            print("Exchange value:" ,float(value) * float(amt) )

country_code = input("Enter country code: ")
amt = input("Enter amount of money in dollar: ")

usd_converter(country_code, amt)


