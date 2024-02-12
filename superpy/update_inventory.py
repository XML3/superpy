import csv
from today import *
from bought import *
from sold import *

#functions to manage inventory updates, from bought to sold and what is in_stock

#read bought data and append it to a list and return the list
def read_bought_data():
    bought_data = []
    with open('bought.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bought_data.append(row)
    return bought_data

#read sold data and append it to a list and return the list
def read_sold_data():
    sold_data = []
    with open('sold.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            sold_data.append(row)
    return sold_data

#calls the data from both bought and sold files
#calculates the current stock based on bought and sold items
def calculate_stock():
    bought_data = read_bought_data()
    sold_data = read_sold_data()
    
    stock = {}
    for item in bought_data:
        product = item['product']
        quantity_bought = int(item['quantity'])
        #updates the `stock` dict. Retrieves the currect quantity of the product from stock, it adds the quantity_bought to esxisting quantity / else zero. = updates the value of `product` key in the `stock` dict.
        stock[product] = stock.get(product, 0) + quantity_bought
        
    for item in sold_data:
        product = item['product']
        quantity_sold = int(item['quantity'])
        #updates the `stock` dict. Retrieves the currect quantity of the product from stock, it subtracts the quantity_sold to esxisting quantity / else zero. = updates the value of `product` key in the `stock` dict.
        stock[product] = stock.get(product, 0) - quantity_sold
        
        return stock
    
    #usage
    stock = calculate_stock()
    print(stock)
    
    