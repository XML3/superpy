# Imports
import argparse
import csv
from datetime import date
from valid_date_fnc import valid_date
from bought import add_purchase
from transactions import *
from sold import *
from inventory import *
from update_inventory import *
from revenue import *

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
    
#Create inventory parser
    inventory_parser = subparsers.add_parser('inventory', help='Select to view inventory')
    inventory_parser.add_argument('product', type=str, help='Product"s name')
    inventory_parser.add_argument('price', type=float, help='Total price')
    inventory_parser.add_argument('purchase_price', type=str, help="Purchasing price of item")
    inventory_parser.add_argument('quantity_bought', type=int, help='Bought quantity of item')
    inventory_parser.add_argument('quantity_sold', type=int, help='Sold quantity of item')
    inventory_parser.add_argument('in_stock', type=int, help='Stock amount of product')
    inventory_parser.add_argument('expiry_date', type=valid_date, help=' Product"s expiration date')
    inventory_parser.add_argument('sale_price', type=float, help='Product"s sale price')
    inventory_parser.add_argument('expiry_status', type=str, help='Expiration date status')
    inventory_parser.add_argument('--date', help='Date to fileter inventory (YYYY-MM-DD)')
#Create inventory_ID parser to retrieve product by ID
    inventory_id_parser = subparsers.add_parser('inventory_id', help='Retrieve a product by ID')
    inventory_id_parser.add_argument('product_id', type=str, help='Product ID')

#Create inventory_update parser
    update_inventory_parser = subparsers.add_parser('update_inventory', help='Update inventory')
    update_inventory_parser.add_argument('product', type=str, help='Product"s name')
    update_inventory_parser.add_argument('quantity_bought', type=int, help='Bought quantity of product')
    update_inventory_parser.add_argument('quantity_sold', type=int, help='Sold quantity of product')
    update_inventory_parser.add_argument('in_stock', type=int, help='Total Stock quantity of product')
    update_inventory_parser.add_argument('--date', help='Date to update inventory (YYY-MM-DD)')
    
#Create revenue parser
    revenue_parser = subparsers.add_parser('revenue', help='Ger revenue information')
    revenue_parser.add_argument('input', choices=['today', 'yesterday', '--date'], help='Specify type of request')
    revenue_parser.add_argument('date', nargs='?', type=str, help='Filter Date or month-year"s revenue (YYYY-MM or YYYY-MM-DD)')


    args = parser.parse_args()
    
    #buy
    if args.command == 'buy':
        add_purchase(args.product, args.price, args.quantity, args.expiration_date, args.purchase_date)
        print("Succesful")

    #sell
    if args.command == 'sell':
      sold_data = prep_sold_data(args.bought_id, args.product, args.sell_price, args.quantity, args.sell_date)
      write_to_csv(sold_data)
      print("Successful Sale")

    #transaction
    
    #inventory_ID
    if args.command == 'inventory_id':
        product_id = args.product_id
        product = get_product_by_id(product_id)
        if product:
            print("Product found:")
            print(product)
    
    #inventory
    if args.command == 'inventory':
        if args.date:
            print("Inventory for date: ", args.date)
            print_inventory_data(args.date)
        else:
            add_inventory(args.product, args.price, args.purchase_price, args.quantity_bought, args.quantity_sold, args.in_stock, args.expiry_date, args.sale_price, args.expiry_status)
            print("Succesful operation!")
        
    #revenue
    if args.command == 'revenue':
        revenue, cost = revenue_requests(args.input, args.date)
        print('Revenue:'. revenue)
        print("Cost:", cost)
    
#inventory_update
    if args.command == 'update_inventory':
        calculate_stock()
    
#advance_time
    if hasattr(args, 'advance_time') and args.advance_time:
        advance_current_date(args.advance_time)
        print('Ok')
        return
    
if __name__ == "__main__":
    main()
