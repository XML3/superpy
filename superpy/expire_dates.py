import csv
from inventory import *
from update_inventory import *
from sold import *
from inventory_utils import *

#Check for products with expired dates compared with today's date, it iterates  through the inventory file  and using a functuion to load the inventory,
# For each item in the inventory, it checks the expiry_date against today's date (using a callback function). 
# It loads the sold data, it compares, checks If item has expired and has been sold, informs and append this to the CSV file


def expired_products_header():
    is_new_file = False
    try:
        with open('expire_dates.csv', 'r') as csvfile:
            is_new_file = csvfile.read().strip() == ''
    except FileNotFoundError:
        is_new_file = True
        
    #write header if new or empty
    if is_new_file:
        with open('expire_dates.csv', 'w', newline='') as csvfile:
            fieldnames = ['product_id', 'product', 'expiry_date', 'expired_sold']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            

def show_all_expired_products():
    inventory = load_inventory()
    
    print("Expired Products:")
    for item in inventory:
        #Check if the product expired
        expiry_date = item['expiry_date']
        if expiry_date < get_current_date():
            print(f"Product ID: {item['product_id']}")
            print(f"Product Name: {item['product']}")
            print(f"Expiry Date: {expiry_date}")
            print()

def expired_products(all_products=False):
    today = get_current_date()
    #load inventory data
    inventory = load_inventory()
    #load sold data
    sold_data = load_sold_data()
    
    with open('expire_dates.csv', 'a', newline='') as csvfile:
        fieldnames = ['product_id', 'product', 'expiry_date', 'expired_sold']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for item in inventory:
            expiry_date_str = item['expiry_date']
            expiry_date_str = expiry_date_str.split()[0]
            expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
            if expiry_date < today:
                #Check if expired product was sold
                product_id = item['product_id']
                product_name = item['product']
                if any(product_id == sold_item['product_id'] or product_name == sold_item['product'] for sold_item in sold_data):
                    #if the expired product was sold, write it to the expired_dates.csv file
                    writer.writerow({'product_id' : item['product_id'], 'product' : item['product'], 'expiry_date': expiry_date, 'expired_sold' : 'yes'})
                    print(f"Product {product_name} has expired and was sold!")
               
                
    return 

        
        
 