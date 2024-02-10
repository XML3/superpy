import csv
import argparse
from create_id import *
from datetime import datetime


#header 
def write_header():
    #Check if file already exists
    is_new_file = False
    try: 
        with open('bought.csv', 'r') as csvfile:
            is_new_file = csvfile.read().strip() == ''
    except FileNotFoundError:
        is_new_file = True
        
        #Write header row if new or empty
    if is_new_file:
        with open('bought.csv', 'w', newline='') as csvfile:
            fieldnames = ['purchase_id', 'product', 'price', 'quantity', 'expiration_date', 'purchase_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    
#Prep Data for CSV function
def add_purchase(product, price, quantity, expiration_date, purchase_date):
    try:
         #Generate unique ID for purchase
        purchase_id = generate_purchase_id()
    
    
        purchase_data = {
            'id': purchase_id,
            'product': product,
            'price': price,
            'quantity': quantity,
            'expiration_date': expiration_date,
            'purchase_date': datetime.now().strftime('%Y-%m-%d')
        }
        #write header if needed
        write_header()
    
    #Append purchase to CSV file
        with open('bought.csv', 'a', newline="") as csvfile:
            fieldnames = ['id', 'product', 'price', 'quantity', 'expiration_date', 'purchase_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow(purchase_data)
        
    except Exception as e:
        print(f"An error occurred while adding purchase: {e}")
    
    #Read and Print content of bought.csv file
def print_bought_data():
    with open('bought.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader: 
            print(row)
                
if __name__ == "__main__":
    #sample purchase
    add_purchase('Orange', 1.50, 3, '2024-02-15')

    print_bought_data()