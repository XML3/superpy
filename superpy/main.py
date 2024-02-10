# Imports
import argparse
import csv
from datetime import date
from valid_date_fnc import valid_date
from bought import add_purchase
from transactions import *
from sold import prep_sold_data

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    parser = argparse.ArgumentParser(description="Welcome to the Super Inventory App!")
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True
    
    #Create buy/bought parser
    buy_parser = subparsers.add_parser('buy', help='Select if purchasing product')
    buy_parser.add_argument('product', type=str, help='Product"s name you wish to purchase')
    buy_parser.add_argument('price', type=float, help='Product"s price per item')
    buy_parser.add_argument('quantity', type=int, help='Chosen amount of items')
    buy_parser.add_argument('expiration_date', type=valid_date, help='Product"s expiration date')
    buy_parser.add_argument('purchase_date', type=valid_date, help='Purchase date (format: YYYY-MM-DD)')
    
#Create sell parser
    sell_parser = subparsers.add_parser('sell', help='Select if selling product')
    sell_parser.add_argument('bought_id', type=str, help='ID of bought item')
    sell_parser.add_argument('product', type=str, help='Product"s name you wish to sell')
    sell_parser.add_argument('sell_price', type=float, help='Product"s price per item')
    sell_parser.add_argument('quantity', type=int, help='Chosen amount of items')
    sell_parser.add_argument('sell_date', type=valid_date, help='Sell date (format: YYYY-MM-DD)')
    
#Create transaction parser
    transaction_parser = subparsers.add_parser('transaction', help="Transaction records from buy and sell transactions")
    #add arguments here
    
    
#Parse Arguments

    args = parser.parse_args()
    
    #buy
    if args.command == 'buy':
        add_purchase(args.product, args.price, args.quantity, args.expiration_date, args.purchase_date)
        print("Succesful")

    #sell
    if args.command == 'sell':
        prep_sold_data(args.bought_id, args.product, args.sell_price, args.quantity, args.sell_date)
        print("Successful Sale")

if __name__ == "__main__":
    main()
