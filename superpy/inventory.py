import csv 
from today import *
from create_id import*
from update_inventory import *

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
def add_inventory(product, price, purchase_price, quantity_bought, quantity_sold, in_stock, expiry_date, sale_price, expiry_status, update_date, product_id=None,):
    try:
        #generate unique ID for each product
        # if product_id is None:
        #     product_id = generate_product_id()
            
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
            'update_date': update_date
        }
        
        #Load inventory - check if product by id already exists (when searched by ID)
        inventory = load_inventory()
        existing_product = get_product_by_id(product_id)
        
        if existing_product:
            print("Product ID already exists. Updating existing product...")
            update_existing_product(product_id, inventory_data)
        else:
                #generate unique ID for each product
            if product_id is None:
                product_id = generate_product_id()
        
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

#Get product by ID
def get_product_by_id(product_id):
    inventory = load_inventory()
    for product in inventory:
        if product['product_id'] == product_id:
            return product
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
   
    add_inventory(product='Apple', price=1.33, purchase_price='4', quantity_bought=2, quantity_sold=3, in_stock=10, expiry_date='2024-10-13', sale_price=1.5, expiry_status='not_expired', update_date='2024-03-03')