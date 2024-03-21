import numpy
import pandas

data = pandas.read_csv("./data/raw/car_data.csv")
data = data[['Car_Name', 'Year', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'Selling_Price', 'Present_Price']]
data = data.drop(columns='Present_Price')



print(data.head(5))