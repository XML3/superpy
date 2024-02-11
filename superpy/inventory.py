import csv 
from today import *
from create_id import*


def current_inventory():
    current_date = get_current_date()
    
    #display inventory
def inventory_header():
    is_new_file = False
    try:
        with open('inventory.csv', 'r') as csvfile:
            is_new_file = csvfile.read().strip() == ''
    except FileNotFoundError:
        is_new_file = True
        
    #write header if new or empty
    if is_new_file:
        with open('inventory.csv', 'w', newline='') as csvfile:
            fieldnames = ['product_id', 'product', 'price', 'quantity_bought', 'quantity_sold', 'in_stock']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
#Prep Data for CSV 
def add_inventory(product, price, quantity_bought, quantity_sold, in_stock):
    try:
        #generate unique ID for each product
        product_id = generate_product_id()
        
        inventory_data = {
            'product_id': product_id,
            'product': product,
            'price': price,
            'quantity_bought': quantity_bought,
            'quantity_sold': quantity_sold,
            'in_stock': in_stock
        }
        #write header if needed
        inventory_header()
        
        #append new inventory to the file
        with open('inventory.csv', 'a', newline='') as csvfile:
            fieldnames = ['product_id', 'product', 'price', 'quantity_bought', 'quantity_sold', 'in_stock']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(inventory_data)
            
    except Exception as e:
        print(f"An error occurred while adding items to inventory: {e}")
        
#Read and Print content of inventory file
def print_inventory_data():
    with open('inventory.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader:
            print(row)
            
if __name__ == "__main__":
    add_inventory('Apple', 1.30, 5, 2, 3)