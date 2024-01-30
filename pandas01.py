# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:14:11 2024

@author: hp
"""

import pandas
'''
file = pandas.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())

file1 = pandas.read_csv("iris.csv")

print(file1)
print(file1.info())
print(file1.describe())

file2 = pandas.read_csv("diab_data.csv")

print(file2)
print(file2.info())
print(file2.describe())
names=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
file3 = pandas.read_csv("housing_data.csv", names=names)

print(file3)
print(file3.info())
print(file3.describe())



'''
file4 = pandas.read_csv("insurance_data.csv", skiprows=5)

print(file4)
print(file4.info())
print(file4.describe())
