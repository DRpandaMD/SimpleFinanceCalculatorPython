# Author: Michael Zarate
# A simple financial calculator
# For personal skills learning

"""" stuff """


class Income(object):
    cash_flow = 0.0

    def __init__(self, income):
        self.income = income


class Expenditures(object):
    total_expenses = 0.0

    def __init__(self, rent, insurance, food, cell_phone, gas, entertainment, utility_bill):
        self.rent = rent
        self.insurance = insurance
        self.food = food
        self.cell_phone = cell_phone
        self.gas = gas
        self.entertainment = entertainment
        self.utility_bill = utility_bill


class Debt(object):
    amount_paid = 0.0
    time_to_pay_off = 0
    interest_total = 0.0
    periods_in_year = 1

    def __init__(self, debt_amount, percentage):
        self.debt_amount = debt_amount
        self.percentage = percentage


class Bank(object):
    savings_added_per_month = 0
    interest_earned = 0.0
    periods_in_year = 1
    leverage_ratio = 0
    total_debts = 0.0
    total_liabilities = 0.0

    def __init__(self, checking, saving, interest_percentage):
        self.checking = checking
        self.saving = saving
        self.interest_percentage = interest_percentage


class Mortgage(object):
    sweep_amount = 0.0
    months_to_pay_off = 0
    saved_on_interest = 0
    periods_in_year = 1
    simple_interest = 0.0

    def __init__(self, mortgage_amount, percentage, length):
        self.mortgage_amount = mortgage_amount
        self.percentage = percentage
        self.length = length


class Menu(object):
    exit_flag = False
    can_calculate_flag = False
    can_write_flag = False

    def print_menu(self):
        print 'Pick from the following menu options: \n \n'
        print '1) \t Edit Current Monthly Income:'
        print '2) \t Edit Mortgage Details:'
        print '3) \t Edit Bank Checking and Savings Accounts Details:'
        print '4) \t Edit Debt Amount'
        print '5) \t Edit Monthly Expenditures'
        print '6) \t Calculate Financial Data'
        print '9) \t Write financial data and statistics to "finances.txt": '
        print '0) \t Exit!'


# Define Functions here
# We will use a list of functions to calculate various types of
# financial data and provide the results to the user

def calc_total_expenses(rent, insurance, food, cell_phone, gas, entertainment, utility_bill):
    expend_total = rent + insurance + food + cell_phone + gas + entertainment + utility_bill
    print "total expenditures = ", expend_total
    return expend_total


def calc_cash_flow(income, expenses):
    print income, expenses
    cash_flow = (income - expenses)
    print 'cash flow is:', cash_flow
    return cash_flow


def calc_simple_interest(principal, interest_rate, period):
    simple_interest = principal * interest_rate * period
    print 'Simple interest is: ', simple_interest
    return simple_interest


def calc_total_debt(debts, mortgage):
    total_debt = debts + mortgage
    print 'Total debts are: ', total_debt
    return total_debt


def calc_total_liabilities(total_debt, total_expenses):
    total_liabilities = total_debt + total_expenses
    print 'Total liability is: ', total_liabilities
    return total_liabilities


def calc_leverage_ratio(total_liabilities, total_income):
    leverage_ratio = total_liabilities / total_income
    print 'My leverage ratio is: ', leverage_ratio
    return leverage_ratio


# initialize my objects first
my_money = Income(0.0)
menu = Menu()
my_mortgage = Mortgage(0.0, 0.0, 0)
my_bank = Bank(0, 0, 0)
my_debt = Debt(0, 0)
my_expenditures = Expenditures(0, 0, 0, 0, 0, 0, 0)

# I made a bunch of objects to hold all the details about my accounts
# I also made an object for my menu so it could just print my menu out
# Then its just a matter of collecting data from the user

while menu.exit_flag is not True:
    menu.print_menu()
    try:
        key = int(raw_input('Enter your choice:'))
        print 'the key is: ', key

        if key is 1:
            my_money.income = float(raw_input("Enter you current monthly income per month \n"))
            print 'My monthly income is: ', my_money.income

        elif key is 2:
            my_mortgage.mortgage_amount = float(raw_input('Enter in your Mortgage amount \n'))
            my_mortgage.length = float(raw_input("Enter in the Length of your Mortgage in months \n"))
            my_mortgage.percentage = float(raw_input("Enter in the percentage on the loan \n"))
            print 'Mortgage: ', my_mortgage.mortgage_amount
            print 'Length in Months: ', my_mortgage.length
            print 'Percent Interest: ', my_mortgage.percentage

        elif key is 3:
            my_bank.checking = float(raw_input('Enter in your checking account balance: \n'))
            my_bank.saving = float(raw_input('Enter in your savings account balance: \n'))
            my_bank.interest_percentage = float(raw_input('Enter in your savings account interest rate: \n '))
            print 'Checking Account Balance: ', my_bank.checking
            print 'Savings Account Balance: ', my_bank.saving
            print 'Savings Account Interest rate is: ', my_bank.interest_percentage

        elif key is 4:
            my_debt.debt_amount = float(raw_input('Enter in your total debt amount: \n'))
            my_debt.percentage = float(raw_input('Enter in the interest percentage on the debt: \n'))
            print 'Debt amount: ', my_debt.debt_amount
            print 'Debt interest rate: ', my_debt.percentage

        elif key is 5:
            my_expenditures.rent = float(raw_input('Enter in your monthly rent amount: \n'))
            my_expenditures.insurance = float(raw_input('Enter in your monthly insurance bill: \n'))
            my_expenditures.cell_phone = float(raw_input('Enter in your monthly cell phone bill: \n'))
            my_expenditures.food = float(raw_input('Enter in how much you spend on food in a month: \n'))
            my_expenditures.gas = float(raw_input('Enter in how much you spend on gas per month: \n'))
            my_expenditures.entertainment = float(raw_input('Enter in how much you spend on entertainment per month: \n'))
            my_expenditures.utility_bill = float(raw_input('Enter in how much your average utility bill is: \n'))
            print 'Rent Bill amount: ', my_expenditures.rent
            print 'Insurance Bill amount: ', my_expenditures.insurance
            print 'Cell Phone Bil amount: ', my_expenditures.cell_phone
            print 'Food budget amount: ', my_expenditures.food
            print 'Gas budget amount: ', my_expenditures.gas
            print 'Entertainment budget amount: ', my_expenditures.entertainment
            print 'Utility Bill amount: ', my_expenditures.utility_bill

        elif key is 6:
            print 'Calculating Financial data please wait: \n'
            my_expenditures.total_expenses = calc_total_expenses(my_expenditures.rent, my_expenditures.insurance,
                                                                 my_expenditures.cell_phone, my_expenditures.food,
                                                                 my_expenditures.gas, my_expenditures.entertainment,
                                                                 my_expenditures.utility_bill)
            my_money.cash_flow = calc_cash_flow(my_money.income, my_expenditures.total_expenses)
            my_bank.interest_earned = calc_simple_interest(my_bank.saving, my_bank.interest_percentage,
                                                           my_bank.periods_in_year)
            my_mortgage.simple_interest = calc_simple_interest(my_mortgage.mortgage_amount, my_mortgage.percentage,
                                                               my_mortgage.periods_in_year)
            my_debt.interest_total = calc_simple_interest(my_debt.debt_amount, my_debt.percentage,
                                                          my_debt.periods_in_year)
            my_bank.total_debts = calc_total_debt(my_debt.debt_amount, my_mortgage.mortgage_amount)
            my_bank.total_liabilities = calc_total_liabilities(my_bank.total_debts, my_expenditures.total_expenses)
            my_bank.leverage_ratio = calc_leverage_ratio(my_bank.total_liabilities, my_money.income)

        elif key is 9:
            print 'Writing Financial data to "finances.txt"!! \n '
            finance_file = open('Finances.txt', 'w')
            finance_file.write("Your total income is: ")
            finance_file.write(str(my_money.income))
            finance_file.write("\n")
            finance_file.write("Your total expenditures are: ")
            finance_file.write(str(my_expenditures.total_expenses))
            finance_file.write("\n")
            finance_file.write("Your positive cash flow is: ")
            finance_file.write(str(my_money.cash_flow))
            finance_file.write("\n")
            finance_file.write("Your simple interest earned on your savings account for the year is: ")
            finance_file.write(str(my_bank.interest_earned))
            finance_file.write("\n \n")
            finance_file.write("Your debts are: ")
            finance_file.write(str(my_debt.debt_amount))
            finance_file.write("\n")
            finance_file.write("The interest paid on the debt is: ")
            finance_file.write(str(my_debt.interest_total))
            finance_file.write("\n")
            finance_file.write("Your mortgage is: ")
            finance_file.write(str(my_mortgage.mortgage_amount))
            finance_file.write("\n")
            finance_file.write("The amount paid on your mortgage interest for the year is: ")
            finance_file.write(str(my_mortgage.simple_interest))
            finance_file.write("\n \n")
            finance_file.write("Your total debt is: ")
            finance_file.write(str(my_bank.total_debts))
            finance_file.write("\n")
            finance_file.write("Your total financial liability is: ")
            finance_file.write(str(my_bank.total_liabilities))
            finance_file.write("\n")
            finance_file.write("Your financial leverage ratio is")
            finance_file.write(str(my_bank.leverage_ratio))
            finance_file.write("\n\n")
            finance_file.write("##EOF##")
            finance_file.close()


        elif key is 0:
            menu.exit_flag = True
            print 'exit flag is now true \n'

        else:
            print 'Please enter a valid option \n '

    except ValueError:
        print 'ERROR: Enter a valid integer \n \n'
else:
    print 'exiting!!\n'
