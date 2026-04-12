
"""
File: checkingaccount.py
This module defines the CheckingAccount class.
"""

from bankaccount import BankAccount

class CheckingAccount(BankAccount):

    def __str__(self):
        result = "Name:    " + self.name + '\n'
        result += "PIN:     " + self.pin + '\n'
        result += "Balance: " + str(self.balance)
        return result
    