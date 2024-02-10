import csv
from create_id import *
from datetime import datetime

#Header:
def write_header():
#check if header exists
    is_new_file = False
    try:
        with open('sold.csv', 'r' ) as csvfile:
            is_new_file = csvfile.read().strip() == ''
    except FileNotFoundError:
        is_new_file = True
        
        #Write header row if new or empty
    if is_new_file:
        with open('sold.csv', 'w', newline='') as csvfile:
            fieldnames = ['sold_id','bought_id', 'product', 'sell_price', 'quantity', 'sell_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
#Prep data for CSV 
def prep_sold_data(bought_id, product, sell_price, quantity, sell_date):
    sold_id = generate_sold_id()
    sell_date = datetime.now().strftime('%Y-%m-%d')
    sold_data = {
        'sold_id': sold_id,
        'bought_id': bought_id,
        'product': product,
        'sell_price': sell_price,
        'quantity': quantity,
        'sell_date': sell_date
    }
    print("Data prepared:", sold_data)
    return sold_data
    
#Write/ append to CSV file
def write_to_csv(sold_data):
    try:
        write_header()
        
        with open('sold.csv', 'a', newline='') as csvfile:
            fieldnames = ['sold_id', 'bought_id', 'product', 'sell_price', 'quantity', 'sell_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(sold_data)
            print("Data written to CSV:", sold_data)
    except Exception as e:
        print("Error writing to CSV:", e)

if __name__ == "__main__":
    bought_id = 'a251e173-3415-490d-bef4-b9d42545e157'
    
    sold_data = prep_sold_data(bought_id, 'Product Orange', 1.45, 3)
    write_to_csv(sold_data)