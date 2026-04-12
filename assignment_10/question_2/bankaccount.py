"""
File: bankaccount.py
This module defines the BankAccount parent class.
"""

class BankAccount:

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin