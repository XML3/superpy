import csv 
from today import *
from create_id import*

#User will also be able to searchh inventory by date 

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
            fieldnames = ['product_id', 'product', 'price', 'quantity_bought', 'quantity_sold', 'in_stock', 'update_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
#Prep Data for CSV 
def add_inventory(product, price, quantity_bought, quantity_sold, in_stock):
    try:
        #generate unique ID for each product
        product_id = generate_product_id()
        update_date = get_current_date()
        
        inventory_data = {
            'product_id': product_id,
            'product': product,
            'price': price,
            'quantity_bought': quantity_bought,
            'quantity_sold': quantity_sold,
            'in_stock': in_stock,
            #User can search invetory by date
            'update_date': update_date
        }
        #write header if needed
        inventory_header()
        
        #append new inventory to the file
        with open('inventory.csv', 'a', newline='') as csvfile:
            fieldnames = ['product_id', 'product', 'price', 'quantity_bought', 'quantity_sold', 'in_stock', 'update_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(inventory_data)
            
    except Exception as e:
        print(f"An error occurred while adding items to inventory: {e}")
        
#Read and Print content of inventory file
def print_inventory_data(date=None):
    with open('inventory.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        
        for row in reader:
            if date is None or row['update_date'] == date:
                print(row)
            
if __name__ == "__main__":
    add_inventory('Apple', 1.30, 5, 2, 3)