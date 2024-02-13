import csv
from today import *

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
        cost_bought - get_cost_bought_for_month(year, month)
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
            if sell_date.startswith('f{year}-{month:02}'):  
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
            if purchase_date.startswith('f{year}-{month:02}'):  
                cost = float(row['purchase_price']) * int(row['quantity'])
                bought_items_cost += revenue
    return bought_items_cost
    
revenue, cost = revenue_requests('today')
print("Revenue today:", revenue)
print('Cost today:', cost)

revenue, cost = revenue_requests('--date', '2019-12')
print("Revenue from December 2019:", revenue)
print('Cost from December 2019:', cost)
