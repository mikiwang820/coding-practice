#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:33:02 2020

@author: wangmeiqi
"""


#Python coed to create BankAccount class
#with deposit() and withdraw() function 
#Reference https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/


class BankAccount:
    
    def __init__(self):
        
        self.balance = 0
        
        print("Welcome to the Deposit & Withdrawal Machine")
        
    def deposit(self):
        
        amount = float(input("Enter amount to be Deposited: "))
        
        self.balance += amount
        
        print("Amount Deposited: ", amount)
        
    def withdraw(self):
        
        amount = float(input("Enter amount to be Deposited: "))
        
        if amount > self.balance:
            
            print("Insufficient balance")
            
        else:
            
            self.balance -= amount
            
            print("You withdrew: ", amount)
            
    def display(self):
        
        print("\n New available balance:", self.balance)
        
#drive code
balance = BankAccount()

balance.deposit()

balance.withdraw()

balance.display()