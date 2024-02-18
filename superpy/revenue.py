import csv
from today import *
from datetime import datetime
from rich.table import Table
from rich.console import Console
from richtable import *

#Rich Table section
def display_revenue(start_date=None, end_date=None):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style= "yellow", justify="center")
    table.add_column('Sold Revenue', style="green", justify="center")
    table.add_column("Buying Cost", style="cyan", justify="center")
    if start_date and end_date:
        table.add_column("Start Date", style="yellow", justify="center")
        table.add_column("End Date", style="cyan", justify="center")
   
    rows_read = False
    
    with open('revenue.csv', 'r' ) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows_read = True  # Set flag to True if rows are read
            add_row(table, row['date'], row['revenue_sold'], row['cost_bought'], start_date, end_date)
    if not rows_read:  # If no rows were read, add a message
            add_row(table, "No data available", "", "", start_date, end_date)
    console.print(table)
        

def write_revenue(revenue_sold, cost_bought):
    with open('revenue.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'revenue_sold', 'cost_bought']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'date': datetime.now().strftime('%Y-%m-%d'),
            'revenue_sold': revenue_sold,
            'cost_bought': cost_bought
        })


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
                cost = float(row['price']) * int(row['quantity'])
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
    
#Get revunue for a specific period of time
def get_revenue_specify_period(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    total_revenue = 0
    
    with open('sold.csv', 'r', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sell_date = datetime.strptime(row['sell_date'], '%Y-%m-%d')
            if start_date <= sell_date <= end_date:
                revenue = float(row['sell_price']) * int(row['quantity'])
                total_revenue += revenue
    return total_revenue
    
