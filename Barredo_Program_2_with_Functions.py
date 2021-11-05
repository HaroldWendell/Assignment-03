# Create a program with functions that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25 pesos. Display the output in the following format.
# The total amount is _______ pesos.

def price_A():
    priceA = 20
    return priceA

def printPriceA(priceA):
    print(f'The price of one apple is {priceA} pesos.')

def Quantity_apples():
    apples = int(input('Quantity of apples to Purchase: '))
    return apples

def price_B():
    priceB = 25
    return priceB

def printPriceB(priceB):
    print(f'The price of one orange is {priceB} pesos.')

def Quantity_oranges():
    oranges = int(input('Quantity of oranges to Purchase: '))
    return oranges

def Total_amount(priceA, apples, priceB, oranges):
    Amount = float(priceA * apples + priceB * oranges)
    return Amount

def displayOutput(Amount):
    print(f'The total amount is {Amount} pesos.')

# Steps
# 1. Print the price of one apple.
priceA = price_A()
printPriceA(priceA)
# 2. Inquire with the user about the quantity of apples to be purchased and save it to a variable.
apples = Quantity_apples()
# 3. Print the price of one apple.
priceB = price_B()
printPriceB(priceB)
# 4. Inquire with the user about the quantity of apples to be purchased and save it to a variable.
oranges = Quantity_oranges()
# 5. Calculate the total amount you must pay.
Amount = Total_amount(priceA, apples, priceB, oranges)
# 6. Display the Output.
displayOutput(Amount)