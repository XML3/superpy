import csv 
from today import *
from create_id import*


#Load inventory data to be used across different function calls
def load_inventory():
    inventory = []
    with open('inventory.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            inventory.append(row)
    return inventory

#User will also be able to search inventory by date 
def current_inventory():
    current_date = get_current_date()
    print_inventory_data(current_date)
    
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
            fieldnames = ['product_id', 'product', 'price', 'purchase_price', 'quantity_bought', 'quantity_sold', 'in_stock', 'expiry_date', 'sale_price', 'expiry_status', 'update_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
#Prep Data for CSV 
def add_inventory(product, price, purchase_price, quantity_bought, quantity_sold, in_stock, expiry_date, sale_price, expiry_status, update_date):
    try:
        #generate unique ID for each product
        product_id = generate_product_id()
        update_date = get_current_date()
        
        inventory_data = {
            'product_id': product_id,
            'product': product,
            'price': price,
            'purchase_price': purchase_price,
            'quantity_bought': quantity_bought,
            'quantity_sold': quantity_sold,
            'in_stock': in_stock,
            'expiry_date': expiry_date,
            'sale_price': sale_price,
            'expiry_status': expiry_status,
            #User can search invetory by date
            'update_date': update_date
        }
        #write header if needed
        inventory_header()
        
        #append new inventory to the file
        with open('inventory.csv', 'a', newline='') as csvfile:
            fieldnames = ['product_id', 'product', 'price', 'purchase_price', 'quantity_bought', 'quantity_sold', 'in_stock', 'expiry_date', 'sale_price', 'expiry_status', 'update_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(inventory_data)
            
    except Exception as e:
        print(f"An error occurred while adding items to inventory: {e}")
        
#Get purchase price for product and call inventory function to read/load data
def get_purchase_price(product, inventory):
    for row in inventory:
        if row['product'] == product:
            return row['price']
    return None

#Get expiry_date call function
def get_expiry_date(product, inventory):
      for row in inventory:
          if row['product'] == product:
              return row['expiry_date']
      return None
  
  #Get sale_price call function      
def get_sale_price(product, inventory):
    for row in inventory:
        if row['product'] == product:
            return row['sale_price']
    return None
    
#Get expirary_status, call function
def get_expiry_status(product, inventory):
    for row in inventory:
        if row['product'] == product:
            return row['expiry_status']
    return None

#Read and Print content of inventory file
def print_inventory_data(date=None):
    with open('inventory.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        
        for row in reader:
            if date is None or row['update_date'] == date:
                print(row)
    
#function to advance the current date by specified number of days        
def advance_time(days):
    advance_current_date(days)
    print('OK')

if __name__ == "__main__":
    add_inventory('Apple', 1.33, '4', 2, 3, 10, '2024-10-13', 1.5, 'not_expired')