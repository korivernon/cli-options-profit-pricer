
CONTRACTS = 100

# Colors
def make_red(st):
    txt = "\033[1;31;40m{string}\033[0m"
    print(txt.format(string = st))

def make_yelo(st):
    txt = "\033[1;33;40m{string}\033[0m"
    print(txt.format(string = st))

def make_purp(st):
    txt = "\033[1;35;40m{string}\033[0m"
    print(txt.format(string = st))

def make_blue(st):
    txt = "\033[1;34;40m{string}\033[0m"
    print(txt.format(string = st))

def make_cyan(st):
    txt = "\033[1;36;40m{string}\033[0m"
    print(txt.format(string = st))

def make_white(st):
    txt = "\033[1;37;40m{string}\033[0m"
    print(txt.format(string = st))

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
    make_white("==============Menu================")
    make_white("*press ENTER/return key to exit*")
    print()
    make_white("1) Call Price Speculator")

def calc_call_price():
    print("==============================")
    tkr = input("\033[1;36;40mTicker Name: \033[0m")
    risk_amt = float(input("\033[1;36;40mHow much do you want to put at risk: \033[0m"))
    buy_price = float(input("\033[1;36;40mPremium purchase price: \033[0m"))

    max_contracts = risk_amt//(buy_price*100)
    print("You can buy a maximum of", max_contracts, tkr, "contracts with", risk_amt,"dollars.")

    buy_in = max_contracts * buy_price * CONTRACTS

    perc_or_money = input("\033[1;36;40mHow do you want to calculate your sale price (p/m): \033[0m")
    

    while ((perc_or_money != 'p' and perc_or_money == 'm') and (perc_or_money == 'p' and perc_or_money != 'm')):
        perc_or_money = input("\033[1;36;40mHow do you want to calculate your sale price (p/m): \033[0m")
    exit_amt = 0
    if perc_or_money == 'p':
       
        perc = float(input("\033[1;31;40mIdealized Percentage Profit: \033[0m"))
        exit_amt = buy_price*(1+(perc/100))
        sale_price = max_contracts * exit_amt * CONTRACTS
    elif perc_or_money == 'm':
        mon = float(input(" \033[1;31;40mIdealized Money Profit: \033[0m"))
        exit_amt = mon/(max_contracts*CONTRACTS)
        sale_price = max_contracts*exit_amt*CONTRACTS
    profit = sale_price-buy_in
    print()
    buy_in_str = "Your risk amount will be: "+ str(buy_in)
    make_yelo(buy_in_str)
    sale_price_str = "Your exit price will be: " + str(exit_amt)
    make_red(sale_price_str)
    print("Your sale price will be:", sale_price, "dollars.")
    profit_str = "Your total profit will be: "+ str(profit)+ " dollars." 
    make_purp(profit_str)

    call_spec = Option(tkr, max_contracts, buy_in, sale_price, profit)
    return call_spec

def take_input():
    make_white("==============================")
    inp = input("What would would you like to select? ")
    return inp

def call_calc():
    make_yelo("Welcome to the Command Line Options Pricer Calculator")
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
    make_red("==========Exiting Interface==========")
    print()
    make_yelo("Here are your speculative calls: ")
    print()
    for i in range(len(ls)):
        print(ls[i])
    make_red("==========Exiting==========")


def main():
    call_calc()
main()
