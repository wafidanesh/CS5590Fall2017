# Superclass of expenses
class Expenses:
    total_expenses = 0  # To store the total expenses

    def __init__(self):  # Welcome to the expense management system
        self.title = 'Expense Managament System'

    def expense_entry(self):  # Type of expense
        exp_name = self.name
        exp_amount = self.amount
        print(self.name)
        print('Amount is ' + self.amount)

    def total_expenditure(self):  # Total expenditure
        Expenses.total_expenses = Expenses.total_expenses + int(self.amount)
        print(Expenses.total_expenses)

    def savings(self,grs_income):  # Total savings
        self.save = grs_income - Expenses.total_expenses
        print(self.save)

# Class for storing the particulars of a person
class Particulars:

    def __init__(self,name,age):
        self.pname = name
        self.page = age

    def get_details(self):
        return self.pname, self.page

# Subclasses detailing expenses
class HouseExp(Expenses):  # House rent expenses
    def __init__(self):
        Expenses.__init__(self)
        self.name = 'Housing'
        hamount = input('How much? ')
        self.amount = hamount

class FoodExp(Expenses):  # Food expenses
    def __init__(self):
        Expenses.__init__(self)
        self.name = 'Food'
        famount = input('How much? ')
        self.amount = famount

class MedExp(Expenses):  # Medical expenses
    def __init__(self):
        Expenses.__init__(self)
        self.name = 'Medical'
        mamount = input('How much? ')
        self.amount = mamount

class ClothExp(Expenses):
    def __init__(self):
        Expenses.__init__(self)
        self.name = 'Clothing'
        camount = input('How much? ')
        self.amount = camount

# Multiple inheritance example
class Expense_Profile(Particulars,HouseExp):
    def __init__(self,name,age):
        HouseExp.__init__(self)
        Particulars.__init__(self,name,age)
        self.__SSN = 2798402245

    def get_expenses(self):
        print('Applicant ' + str(self.pname), 'Age ' + str(self.page))
        print(self.name + ' expense is',self.amount)

New = Expense_Profile('Raphael',29)
New.get_expenses()
New.__SSN  # Trying to access the private class




