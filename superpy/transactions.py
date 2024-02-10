import csv
from datetime import datetime

#This function records the transaction details to CSV file
def record_transaction(product, quantity, price, date, transaction_type):
    transaction_data = {
        'product': product,
        'quantity': quantity,
        'price': price,
        'date': date.strftime('%Y-%m-%d'),
        'transaction_type': transaction_type
    }
    
    with open('transactions.csv', 'a', newline='') as csvfile:
        fieldnames = ['product', 'quantity', 'price', 'date', 'transaction_type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(transaction_data)
        
 #The buy and sell product functions handle buying and selling transactions and call the above function to records the transaction data.       
def buy_product(product, quantity, price, date):
    record_transaction(product, quantity, price, date, 'buy')
    #Implement/intergrate logic to update inventory for buy
    
def sell_product(product, quantity, price, date):
    record_transaction(product, quantity, price, date, 'sell')
     #Implement/intergrate logic to update inventory for selling
    
    
    