#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:52:12 2020

@author: wangmeiqi
"""
#Reference https://www.learncodewithmike.com/2020/01/python-inheritance.html

import numpy as np

import pandas as pd


grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}


class MyDataFrame(pd.DataFrame): #Inherit 
    
    def identity_mapping(self):
        
        return self
    
result = MyDataFrame(grades)

print(isinstance(result, MyDataFrame)) #判斷物件與類別的關係


##############################################################################

#Inheritance

#DRY don't repeat yourself

#交通工具 base class

class Transportation:
    
   #constructor 
   def __init__(self):
       
       self.color = "white" #attribution

    #駕駛方法
   def drive(self):
        
      print("Drive method is called")

#car's subclass
class Car(Transportation):
    
    #method
    def accelerate(self):
        
        print("accelerate method is called")
        
        
#airplane's subclass
class Airplane(Transportation):
    
    #method
    def fly(self):
        
        print("fly method is called")    
        
toyota = Car()

toyota.drive() #print

toyota.accelerate()

plane = Airplane()

plane.fly() #print


##############################################################################

#Method overriding

#base class and sub class have the same name of method
class Bike(Transportation):
    
    def drive(self):
        
        print("sub method is called")
        
bicycle = Bike()

bicycle.drive() #print

#opertate the method in the base class
class Motocycle(Transportation):
    
    def drive(self):
        
        super().drive()
        
        print("sub method is called")
        
moto = Motocycle()

moto.drive() #print


##############################################################################

#Multi-Level Inheritance
#繼承(Inheritance)在程式碼的重用(Reusable)上非常好
#但是如果沒有適當的使用就會像此範例一樣產生邏輯上的錯誤（鴨子不會飛）
#建議不超過兩層，否則反而會增加程式碼的複雜度及難以維護

class Animal:
    
    pass

class Bird(Animal):
    
    def fly(self):
        
        print("fly!!!")
        
class Duck(Bird):
    
    pass

duck = Duck()

duck.fly()


##############################################################################

#Multiple Inheritance
#須避免個廢別裡有相同名稱之方法

class Animal:
    
    def walk(self):
        
        print("it can walk")

class Bird:
    
    def eat(self):
        
        print("it can eat")

class Duck(Animal, Bird):
    
    pass
        
duck = Duck()

duck.walk()

duck.eat()
