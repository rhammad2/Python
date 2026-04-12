"""
File: checkingaccount.py
copy the CheckingAccount class from question_2/checkingaccount.py and paste it here.
"""

from bankaccount import BankAccount

class CheckingAccount(BankAccount):

    def __str__(self):
        result = "Name:    " + self.name + '\n'
        result += "PIN:     " + self.pin + '\n'
        result += "Balance: " + str(self.balance)
        return result