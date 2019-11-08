import sys
import math
import requests
import os


# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))


r = requests.get("https://coreyms.com")
print(r.status_code)

# name = input("Your Name? ")
# print("Hello ,", name)
