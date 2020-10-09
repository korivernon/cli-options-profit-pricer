
CONTRACTS = 100

# Option(max_contracts, buy_in, sale_price, profit)

class Option:
    def __init__(self, tkr, max_cont, buy_in, sale_price, profit):
        self.buy = buy_in
        self.tkr = tkr
        self.sale = sale_price
        self.profit = profit
        self.max = max_cont
    def __repr__(self):
        ret = str(self.tkr)+" Option with buy in price of "+ str(self.sale)+" dollars, sale price of "+str(self.sale)+" dollars and profit of "+ str(self.profit)+" dollars."
        return ret
    def __str__(self):
        ret = str(self.tkr)+" Option with buy in price of "+ str(self.sale)+" dollars, sale price of "+str(self.sale)+" dollars and profit of "+ str(self.profit)+" dollars."
        return ret
def print_menu():
    print("==============Menu================")
    print("*press ENTER/return key to exit*")
    print()
    print("1) Call Price Speculator")

def calc_call_price():
    print("==============================")
    tkr = input("Ticker Name: ")
    risk_amt = float(input("How much do you want to put at risk: "))
    buy_price = float(input("Premium purchase price: "))

    max_contracts = risk_amt//(buy_price*100)
    print("You can buy a maximum of", max_contracts, tkr, "contracts with", risk_amt,"dollars.")

    buy_in = max_contracts * buy_price * CONTRACTS

    perc_or_money = input("How do you want to calculate your sale price (p/m): ")

    while ((perc_or_money != 'p' and perc_or_money == 'm') and (perc_or_money == 'p' and perc_or_money != 'm')):
        perc_or_money = input("How do you want to calculate your sale price (p/m): ")
    exit_amt = 0
    if perc_or_money == 'p':
        perc = float(input("Idealized Percentage Profit: "))
        exit_amt = buy_price*(1+(perc/100))
        sale_price = max_contracts * exit_amt * CONTRACTS
    elif perc_or_money == 'm':
        mon = float(input("Idealized Money Profit: "))
        exit_amt = mon/(max_contracts*CONTRACTS)
        sale_price = max_contracts*exit_amt*CONTRACTS
    profit = sale_price-buy_in
    print()
    print("Your risk amount will be:", buy_in)
    print("Your exit price will be:", exit_amt)
    print("Your sale price will be:", sale_price, "dollars.")
    print("Your total profit will be:", profit, "dollars." )

    call_spec = Option(tkr, max_contracts, buy_in, sale_price, profit)
    return call_spec

def take_input():
    print("==============================")
    inp = input("What would would you like to select? ")
    return inp

def call_calc():
    print("Welcome to the Command Line Options Pricer Calculator")
    print_menu()
    inp = take_input()
    ls = []
    while inp != '':
        if inp == "1":
            item = calc_call_price()
        ls.append(item)
        print_menu()
        inp = take_input()

    print()
    print("==========Exiting Interface==========")
    print()
    print("Here are your speculative calls: ")
    for i in range(len(ls)):
        print(ls[i])

    print("==========Exiting==========")
def main():
    call_calc()
main()
