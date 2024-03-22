import numpy
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("./data/raw/car_data.csv")
data = data[['Car_Name', 'Year', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'Selling_Price', 'Present_Price']]
data = data.drop(columns='Present_Price')

dummies_transmission = pandas.get_dummies(data['Transmission'])
data = pandas.concat([dummies_transmission, data], axis=1)
data = data.drop(columns='Transmission')

dummies_fuel_type = pandas.get_dummies(data['Fuel_Type'], prefix='Fuel')
data = pandas.concat([dummies_fuel_type, data], axis=1)
data = data.drop(columns='Fuel_Type')

dummies_seller_type = pandas.get_dummies(data['Seller_Type'], prefix='Seller')
data = pandas.concat([dummies_seller_type, data], axis=1)
data = data.drop(columns='Seller_Type')

print(data.head(10))