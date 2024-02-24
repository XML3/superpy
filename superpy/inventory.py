import csv 
from today import *
from create_id import*
from inventory_utils import *
from update_inventory import *
from datetime import datetime
from rich.table import Table

from rich.console import Console
from richtable import *

#Rich Table section
def display_inventory():
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Product ID", style= "blue", justify="center")
    table.add_column('Product', style="cyan", justify="center")
    table.add_column("Price", style="green", justify="center")
    table.add_column("Purchase Price", style="yellow", justify="center")
    table.add_column("Quantity Bought", style="cyan", justify="center")
    table.add_column("Quantity Sold", style="blue", justify="center")
    table.add_column("In Stock", style="green", justify="center")
    table.add_column("Expiry Data", style="red", justify="center")
    table.add_column("Created Date", style="yellow", justify="center")
    
    
    with open('inventory.csv', 'r' ) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_row(table, row['product_id'], row['product'], row['price'], row['purchase_price'], row['quantity_bought'], row['quantity_sold'], row['in_stock'], row['expiry_date'], row['created_date'])
        console.print(table)
    
    #this will update the inventory with the newly bought items in the bought file
    # display_bought()
        
#User will also be able to search inventory by date 
def current_inventory():
    current_date = get_current_date()
    print_inventory_data(current_date)
    
    #display inventory
def inventory_header():
    try:
        with open('inventory.csv', 'r') as csvfile:
            # check if file is empty
            if csvfile.read().strip() == '':
                #if file is empty, write header
                with open('inventory.csv', 'w', newline='') as csvfile:
                    fieldnames = ['product_id', 'product', 'price', 'purchase_price', 'quantity_bought', 'quantity_sold', 'in_stock', 'expiry_date', 'sale_price', 'expiry_status', 'purchase_date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
    except FileNotFoundError as e:
       print(f"Error occurred while accessing file: {e}")
        

             
#Prep Data for CSV 
def add_inventory(product, price, purchase_price, quantity_bought, quantity_sold, in_stock, expiry_date, sale_price, expiry_status, purchase_date, product_id=None,):
    try:
        #generate unique ID for each product
        # if product_id is None:
        #     product_id = generate_product_id()
            
        # created_date = get_current_date()

        
        inventory_data = {
            'product_id': product_id if product_id else generate_product_id(),
            'product': product,
            'price': price,
            'purchase_price': purchase_price,
            'quantity_bought': quantity_bought,
            'quantity_sold': quantity_sold,
            'in_stock': in_stock,
            'expiry_date': expiry_date,
            'sale_price': sale_price,
            'expiry_status': expiry_status,
            'purchase_date': purchase_date
        }
        
        #Load inventory - check if product by id already exists (when searched by ID)
        inventory = load_inventory()
        existing_product = get_product_by_id(inventory_data['product_id'])
        
        if existing_product:
            print("Product ID already exists. Updating existing product...")
            update_existing_product(inventory_data['product_id'], inventory_data)
        else:
            print('Adding new product to inventory...')
            #Append new inventory to the file
            with open('inventory.csv', 'a', newline='') as csvfile:
                fieldnames = ['product_id', 'product', 'price', 'purchase_price', 'quantity_bought', 'quantity_sold', 'in_stock', 'expiry_date', 'sale_price', 'expiry_status', 'purchase_date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(inventory_data)
        
        #write header if needed
        inventory_header()
        

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
def print_inventory_data(search_date=None):
    try:
        with open('inventory.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            header = next(reader)
            print(header)

            for row in reader:
                row_date = datetime.strptime(row['created_date'].split()[0], '%Y-%m-%d').date()
                if search_date is None or row_date == datetime.strptime(search_date, '%Y-%m-%d').date():
                    print("Matching row: ", row)
                else: 
                    print("Non-matching row: ", row)
    except StopIteration:
        print("Inventory is empty")
        
        
#function to advance the current date by specified number of days        
def advance_time(days):
    advance_current_date(days)
    print('OK')

