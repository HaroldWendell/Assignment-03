# Create a program with functions which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy _____ apples and your change is _____ pesos.

def AmountOfCash():
    money = int(input('Amount of cash you have: '))
    return money

def PriceOfApple():
    price = int(input('Price of an apple: '))
    return price

def Max_apples(money, price):
    Max_apples = int(money/price)
    return Max_apples

def rem_money(money, Maximum_apples_you_can_buy, price):
    remaining_money = float(money-(Maximum_apples_you_can_buy*price))
    return remaining_money

def displayMaxAppleCanBuy(Maximum_apples_you_can_buy):
    print(f'Maximum apple you can buy: {Maximum_apples_you_can_buy} pieces.')

def displayRemainingCash(remaining_money):
    (f'Your remaining money will be: {remaining_money} pesos.')

def displayMaxApple_Change(Maximum_apples_you_can_buy, remaining_money):
    print(f'You can buy {Maximum_apples_you_can_buy} apples and your change is {remaining_money} pesos.')

# Steps
# 1. Inquire with the user about the amount of money he/she have and save it to a variable
money = AmountOfCash()
# 2. Inquire with the user about the price of a apple.
price = PriceOfApple()
# 3. Calculate the maximum number of apples you can buy.
Maximum_apples_you_can_buy = Max_apples(money, price)
# 4. Calculate the remaining money that you will have.
remaining_money = rem_money(money, Maximum_apples_you_can_buy, price)
# 5. Display the output of maximum numbers of apples you can buy.
displayMaxAppleCanBuy(Maximum_apples_you_can_buy)
# 6. Display the output of remaining money that you will have.
displayRemainingCash(remaining_money)
# 7. Display the output of maximum numbers of apples you can buy and remaining money that you will have.
displayMaxApple_Change(Maximum_apples_you_can_buy, remaining_money)