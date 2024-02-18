# Imports
import argparse
import csv
from datetime import date
from valid_date_fnc import valid_date
from bought import add_purchase
from sold import *
from inventory import *
from update_inventory import *
from revenue import *
from expire_dates import *
from richtable import create_table, add_row




# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


#Console instance for error = Red
err_console = Console(stderr=True, style="red bold")

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
    
#Create invetory parser to retrieve all inventory data
    inventory_parser = subparsers.add_parser('inventory', help="Retireve all inventory data")
    inventory_parser.add_argument('--date',type=str, help='Date to filter inventory retrieval (YYYY-MM_DD)')

    
#Create add_inventory parser to add new inventory items 
    add_inventory_parser = subparsers.add_parser('add_inventory', help='Add new products to inventory')
    add_inventory_parser.add_argument('product', type=str, help='Product"s name')
    add_inventory_parser.add_argument('price', type=float, help='Total price')
    add_inventory_parser.add_argument('purchase_price', type=str, help="Purchasing price of item")
    add_inventory_parser.add_argument('quantity_bought', type=int, help='Bought quantity of item')
    add_inventory_parser.add_argument('quantity_sold', type=int, help='Sold quantity of item')
    add_inventory_parser.add_argument('in_stock',  type=int, help='Stock amount of product')
    add_inventory_parser.add_argument('expiry_date', type=valid_date, help=' Product"s expiration date')
    add_inventory_parser.add_argument('sale_price',  type=float, help='Product"s sale price')
    add_inventory_parser.add_argument('expiry_status', type=str, help='Expiration date status')
    add_inventory_parser.add_argument('--created_date', type=str, help='Date to fileter inventory (YYYY-MM-DD)')

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
    update_inventory_parser.add_argument('--sale_price', type=float, help='Sale price', default=None) 
#Create revenue parser
    revenue_parser = subparsers.add_parser('revenue', help='Get revenue information')
    revenue_parser.add_argument('input', nargs='?', choices=['today', 'yesterday'], default='today', help='Specify type of request (default: today)')
    revenue_parser.add_argument('--date', type=str, help='Filter Date or month-year"s revenue (YYYY-MM or YYYY-MM-DD)')
    revenue_parser.add_argument('--start_date', type=str, help='Start date for period (YYYY-MM-DD)')
    revenue_parser.add_argument('--end_date',  type=str, help='End date for period (YYYY-MM-DD)')
    
#Create expired_product
    expire_dates_parser = subparsers.add_parser('expire_dates', help='Expired products, were they sold?')
    expire_dates_parser.add_argument('product_id', type=str, nargs='?', help='Product ID')
    expire_dates_parser.add_argument('product', type=str, nargs='?', help='Product"s name')
    expire_dates_parser.add_argument('expiry_date', nargs='?', help='Product"s expiration date')
    expire_dates_parser.add_argument('expired_sold', nargs='?', type=str, help='Indicates if the expired product was sold')
    expire_dates_parser.add_argument('--all', '-a', action='store_true', help='Show all expired products ')
    
    
    args = parser.parse_args()
    print(args)
    
    #buy : adds purchase for bought items to bought.csv, generates new ID 
    if args.command == 'buy':
        add_purchase(args.product, args.price, args.quantity, args.expiration_date, args.purchase_date)
        print("Succesful")
        
        display_bought()

    #sell
    if args.command == 'sell':
      sold_data = prep_sold_data(args.bought_id, args.product, args.sell_price, args.quantity, args.sell_date)
      write_to_csv(sold_data)
      print("Successful Sale")
      display_sold()
    #transaction
    
    #inventory_ID
    if args.command == 'inventory_id':
        product_id = args.product_id
        product = get_product_by_id(product_id)
        if product:
            print("Product found:")
            print(product)
            display_inventory()
    
   #inventory retrieval (all or by date)
    if args.command == 'inventory':
        if args.date:
            print("Inventory for date: ", args.date)
            print_inventory_data(args.date)
        else:
           print('Full inventory: ')
           print_inventory_data(None)
           
           display_inventory()
           
    #Add new items to inventory 
    if args.command == 'add_inventory':
        add_inventory(args.product, args.price, args.purchase_price, args.quantity_bought, args.quantity_sold, args.in_stock, args.expiry_date, args.sale_price, args.expiry_status, args.created_date)
        display_inventory()
            
    #revenue
    if args.command == 'revenue':
        if args.start_date and args.end_date:
                revenue = get_revenue_specify_period(args.start_date, args.end_date)
                print('Revenue for the specified period: ', revenue)
                display_revenue(args.start_date, args.end_date)
        elif args.date:
            revenue, cost = revenue_requests('--date', args.date)
            print('Revenue:', revenue)
            print("Cost:", cost)
        else: 
            revenue, cost = revenue_requests(args.input)
            print('Revenue: ', revenue)
            print("Cost:", cost)
            
            display_revenue()
    
#inventory_update
    if args.command == 'update_inventory':
        if args.product and args.quantity_bought and args.quantity_sold and args.in_stock:
           #preps for new data
            new_data = {
                'product': args.product,
                'quantity_bought': args.quantity_bought,
                'quantity_sold': args.quantity_sold,
                'in_stock': args.in_stock,
                'sale_price': args.sale_price
            }
         #updates exisiting product in the inventory
            update_existing_product(args.product, new_data)
            print("Inventory updated successfully.")
        else: 
            print("Missing required arguments.")

            
        
#expire_date
    if args.command == 'expire_dates':
        if args.all:
             display_expire_dates()
        else: 
            err_console.print("The provided arguments are not valid")

           
    
    
#advance_time
    if hasattr(args, 'advance_time') and args.advance_time:
        advance_current_date(args.advance_time)
        print('Ok')
        return
    
if __name__ == "__main__":
    main()
