import csv
from today import *
from rich_utils import RichUtils

#style tables
rich = RichUtils()

rich.print_styled_text("Revenue Table", style='bold yellow')

header = '[blue]Revenue Today[/blue]  |  [blue]Cost Today[/blue]  |  [blue]Revenue from Month and Year[/blue]  | [blue]Cost from Month and Year[/blue]  |  [blue]Yesterda"s Revenue[/blue]  |  [blue]Yesterda"s Cost[/blue]' 
rich.print_styled_text(header) 


def revenue_requests(input, date=None):
    if input == 'today':
        if date is None:
            date = get_current_date()
        revenue_sold = get_revenue_sold_items(date)
        cost_bought = get_cost_bought_items(date)
        return revenue_sold, cost_bought
    elif input == 'yesterday':
        yesterday = get_current_date() 
        advance_current_date(-1) #move current date back by 1
        revenue_sold = get_revenue_sold_items(get_current_date())
        cost_bought = get_cost_bought_items(get_current_date())
        #reset current date to original value
        advance_current_date(1)
        return revenue_sold, cost_bought
    elif input == '--date':
        year_month = date.split('-')
        year = int(year_month[0])
        month = int(year_month[1])
        revenue_sold = get_revenue_sold_for_month(year, month)
        cost_bought = get_cost_bought_for_month(year, month)
        return revenue_sold, cost_bought
    else:
        raise ValueError("Invalid input")
    
#functions for revenue calculations

#sold items
def get_revenue_sold_items(date):
    date_str = date.strftime('%Y-%m-%d')
    sold_items_revenue = 0
        
        #read/loop through the csv file/check for today's date, if today = multiply the sell price with quantity
    with open('sold.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['sell_date'] == date_str:
                revenue = float(row['sell_price']) * int(row['quantity'])
                sold_items_revenue += revenue
    return sold_items_revenue

#bought items
def get_cost_bought_items(date):
    date_str = date.strftime('%Y-%m-%d')
    bought_items_cost = 0
    
    with open('bought.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            if row['purchase_date'] == date_str:
                cost = float(row['purchase_price']) * int(row['quantity'])
                bought_items_cost += cost
    return bought_items_cost

def get_revenue_sold_for_month(year, month):
    sold_items_revenue = 0
    with open('sold.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            sell_date = row['sell_date']
            sell_date_year, sell_date_month, _ = sell_date.split('-')
            if int(sell_date_year) == year and int(sell_date_month) == month:
            
                revenue = float(row['sell_price']) * int(row['quantity'])
                sold_items_revenue += revenue
    return sold_items_revenue

#Get revenue for specific month and year logic
def get_cost_bought_for_month(year, month):
    bought_items_cost = 0
    with open('bought.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            purchase_date = row['purchase_date']
            purchase_date_year, purchase_date_month, _ = purchase_date.split('-')
            if int(purchase_date_year) == year and int(purchase_date_month) == month: 
                cost = float(row['price']) * int(row['quantity'])
                bought_items_cost += cost
    return bought_items_cost
    
